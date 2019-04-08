<template>
    <el-row class="group-list-wrap">

        <el-col :xs="{span:24}"
                :sm="{span:24}"
                :lg="{span:20,offset:2}">
            <div class="group-list-menu">
                <el-select
                        class="order"
                        v-model="params.type"
                        placeholder="按类别筛选"
                        @change="getOrUpdateGroupInfo()"
                        clearable>
                    <el-option
                            v-for="item in options"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                    </el-option>
                </el-select>

                <el-input class="search" placeholder="搜索..." v-model="params.search">
                    <el-button slot="append"
                               icon="el-icon-search"
                               @click="getOrUpdateGroupInfo()">
                        搜索
                    </el-button>
                </el-input>

                <el-button
                        class="clearBtn"
                        icon="el-icon-delete"
                        @click="clearSearch();getOrUpdateGroupInfo();">清空搜索
                </el-button>

                <router-link :to="{name : 'addNewGroup'}">
                    <el-button
                            class="addBtn"
                            icon="el-icon-plus"
                            type="primary">
                        新建用户组
                    </el-button>
                </router-link>
            </div>

            <el-table
                    :data="tableData"
                    @sort-change="sortChange"
                    v-loading="tableLoading"
                    element-loading-text="拼命加载中"
                    element-loading-spinner="el-icon-loading"
                    element-loading-background="rgba(0, 0, 0, 0.8)">
                <el-table-column
                        label="#"
                        type="index"
                        prop="number"
                        align="center">
                </el-table-column>
                <el-table-column
                        label="用户组名称"
                        prop="name"
                        align="center">
                    <template slot-scope="scope">
                        <span>{{ scope.row.name }}</span>
                    </template>
                </el-table-column>
                <el-table-column
                        label="人数"
                        prop="usersCount"
                        align="center">
                    <template slot-scope="scope">
                        <span>{{ scope.row.users_count }}</span>
                    </template>
                </el-table-column>
                <el-table-column
                        label="类别"
                        prop="type"
                        align="center">
                    <template slot-scope="scope">
                    <span>
                        {{ scope.row.type | formatterType}}</span>
                    </template>
                </el-table-column>
                <el-table-column
                        label="创建日期"
                        sortable="custom"
                        prop="created_datetime"
                        align="center">
                    <template slot-scope="scope">
                        <i class="el-icon-time"></i>
                        <span>
                        {{ scope.row.created_datetime}}</span>
                    </template>
                </el-table-column>
                <el-table-column
                        label="上次修改日期"
                        sortable="custom"
                        prop="last_modified_datetime"
                        align="center">
                    <template slot-scope="scope">
                        <i class="el-icon-time"></i>
                        <span>
                        {{ scope.row.last_modified_datetime}}</span>
                    </template>
                </el-table-column>
                <el-table-column
                        label="操作"
                        prop="operation"
                        align="center">
                    <template slot-scope="scope">
                        <el-button
                                type="info"
                                size="mini"
                                @click="handleEdit(scope.$index, scope.row)">
                            编辑
                        </el-button>
                    </template>
                </el-table-column>
            </el-table>

            <el-pagination
                    @size-change="getOrUpdateGroupInfo()"
                    @current-change="getOrUpdateGroupInfo()"
                    :current-page.sync="params.page"
                    :page-size="20"
                    layout="total, prev, pager, next, jumper"
                    :total="count">
            </el-pagination>
        </el-col>

    </el-row>
</template>

<script>
    import api from '../../api'

    export default {
        name: "GroupList",
        data() {
            return {
                params: {
                    page: 1,
                    search: '',
                    type: '',
                    ordering: '',
                },
                options: [],
                tableData: [],
                count: 1,
                tableLoading: true,
            }
        },
        mounted() {
            api.getUserGroupType().then(data => {
                this.options = data;
            });
            this.getOrUpdateGroupInfo()
        },
        methods: {
            handleEdit(index, row) {
                this.$router.push({name: 'editUserGroup', params: {id: row.id}});
            },
            getOrUpdateGroupInfo() {
                this.tableLoading = true;
                api.getUserGroup(this.params).then(data => {
                    this.tableData = data.results;
                    this.count = data.count;
                    this.tableLoading = false;
                });
            },
            clearSearch() {
                this.params.search = '';
            },
            sortChange(col) {
                if (col.order === 'ascending') {
                    this.params.ordering = col.prop;
                } else if (col.order === 'descending') {
                    this.params.ordering = '-' + col.prop;
                } else {
                    this.params.ordering = '';
                }
                this.getOrUpdateGroupInfo();
            },
        },
        filters: {
            formatterType(value) {
                if (value === 'NONEEDLOGIN') return '不需要登陆';
                else if (value === 'ALREADYSIGNIN') return '需要登陆已注册';
                else return '需要登陆未注册';
            }
        }
    }
</script>

<style lang="stylus">
    .group-list-wrap {
        width 100%
        height 100%

        .group-list-menu {
            width 100%
            height 40px
            margin 0 auto
            margin-top 20px

            .order {
                width 160px
            }

            .search {
                width 250px
                margin-left 10px
            }

            .clearBtn {
                margin-left 10px
            }

            .addBtn {
                float right
                right 0
            }
        }

        .el-table {
            margin 0 auto
            margin-top 30px
            width 100%
        }

        .el-pagination {
            width 100%
            margin-top 40px
            margin-bottom 20px
        }
    }
</style>
