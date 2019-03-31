<template>
    <div class="group-list-wrap">

        <div class="group-list-menu">
            <div class="group-list-menu-left">
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
                        @click="clearTypeAndSearch();getOrUpdateGroupInfo();">清空搜索
                </el-button>
            </div>

            <div class="group-list-menu-right">
                <router-link :to="{name : 'addNewGroup'}">
                    <el-button
                            class="add-btn"
                            icon="el-icon-plus"
                            type="primary">
                        新建用户组
                    </el-button>
                </router-link>
            </div>
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
                    <span style="margin-left: 10px">{{ scope.row.name }}</span>
                </template>
            </el-table-column>
            <el-table-column
                    label="人数"
                    prop="usersCount"
                    align="center">
                <template slot-scope="scope">
                    <span style="margin-left: 10px">{{ scope.row.users_count }}</span>
                </template>
            </el-table-column>
            <el-table-column
                    label="类别"
                    prop="type"
                    align="center">
                <template slot-scope="scope">
                    <span style="margin-left: 10px">
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
                    <span style="margin-left: 10px">
                        {{ scope.row.created_datetime | formatterDatetime}}</span>
                </template>
            </el-table-column>
            <el-table-column
                    label="上次修改日期"
                    sortable="custom"
                    prop="last_modified_datetime"
                    align="center">
                <template slot-scope="scope">
                    <i class="el-icon-time"></i>
                    <span style="margin-left: 10px">
                        {{ scope.row.last_modified_datetime | formatterDatetime}}</span>
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
    </div>
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
                console.log(index, row);
                //TODO
            },
            getOrUpdateGroupInfo() {
                this.tableLoading = true;
                api.getUserGroup(this.params).then(data => {
                    this.tableData = data.results;
                    this.count = data.count;
                    this.tableLoading = false;
                });
            },
            clearTypeAndSearch() {
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
            },
            formatterDatetime(value) {
                return value.substring(0, 10) + " " + value.substring(11, 19);
            },
        }
    }
</script>

<style lang="stylus">
    .group-list-wrap {
        width 100%
        height 100%

        .group-list-menu {
            width 85%
            height 40px
            margin 0 auto
            margin-top 20px

            .group-list-menu-left {
                float left
                left 0

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
            }

            .group-list-menu-right {
                float right
                right 0
            }
        }

        .el-table {
            margin 0 auto
            margin-top 30px
            width 85%
        }

        .el-pagination {
            margin 0 auto
            width 85%
            margin-top 40px
            margin-bottom 20px
        }
    }
</style>
