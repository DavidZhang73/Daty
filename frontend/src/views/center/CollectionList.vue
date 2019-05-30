<template>
    <el-row class="collection-list-wrap">
        <el-col :xs="{span:24}"
                :sm="{span:24}"
                :lg="{span:24}">
            <el-row :gutter="10" class="collection-list-menu">
                <el-col v-bind="layout">
                    <router-link :to="{name : 'addNewCollection'}">
                        <el-button
                                class="addBtn"
                                icon="el-icon-plus"
                                type="primary">
                            新建文件集
                        </el-button>
                    </router-link>
                </el-col>
                <el-col v-bind="layout">
                    <el-select class="order"
                               placeholder="按时间排序"
                               v-model="params.ordering"
                               @change="getOrUpdateCollectionList()"
                               clearable>
                        <el-option
                                v-for="item in options"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value">
                        </el-option>
                    </el-select>
                </el-col>
                <el-col v-bind="layout">
                    <el-input class="search" placeholder="搜索..." v-model="params.search">
                        <el-button slot="append"
                                   icon="el-icon-search"
                                   @click="getOrUpdateCollectionList()">
                            搜索
                        </el-button>
                    </el-input>
                </el-col>
                <el-col v-bind="layout">
                    <el-button
                            class="clearBtn"
                            icon="el-icon-delete"
                            @click="clearSearch();getOrUpdateCollectionList();">清空搜索
                    </el-button>
                </el-col>
            </el-row>

            <el-table :data="tableData"
                      @sort-change="sortChange"
                      v-loading="false"
                      element-loading-text="拼命加载中"
                      element-loading-spinner="el-icon-loading"
                      element-loading-background="rgba(255, 255, 255, 1)">
                <el-table-column
                        label="#"
                        type="index"
                        prop="number"
                        align="center">
                </el-table-column>
                <el-table-column
                        label="文件集名称"
                        prop="name"
                        align="center">
                    <template slot-scope="scope">
                        {{scope.row.name}}
                    </template>
                </el-table-column>
                <el-table-column
                        label="创建人"
                        prop="creator"
                        align="center">
                    <template slot-scope="scope">
                        {{scope.row.creator}}
                    </template>
                </el-table-column>
                <el-table-column
                        label="类别"
                        prop="type"
                        align="center">
                    <template slot-scope="scope">
                        {{scope.row.type | formatterType}}
                    </template>
                </el-table-column>
                <el-table-column
                        label="创建日期"
                        prop="created_datetime"
                        align="center">
                    <template slot-scope="scope">
                        <i class="el-icon-time"></i>
                        <span>
                        {{ scope.row.created_datetime}}</span>
                    </template>
                </el-table-column>
                <el-table-column
                        label="截至日期"
                        prop="ending_datetime"
                        align="center">
                    <template slot-scope="scope">
                        <i class="el-icon-time"></i>
                        <span>
                        {{ scope.row.ending_datetime}}</span>
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
                                @click="handleEdit(scope.$index, scope.row)"
                                v-if="scope.row.id === $store.state.user.id">
                            编辑
                        </el-button>
                        <el-button
                                style="margin-left: 3px;"
                                type="primary"
                                size="mini"
                                @click="handleSubFile(scope.$index, scope.row)">
                            提交
                        </el-button>
                    </template>
                </el-table-column>
            </el-table>

            <el-pagination
                    @size-change="getOrUpdateCollectionList()"
                    @current-change="getOrUpdateCollectionList()"
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
        name: "CollectionList",
        data() {
            return {
                layout: {
                    xs: {span: 24},
                    sm: {span: 12},
                    lg: {span: 6}
                },
                params: {
                    page: 1,
                    search: '',
                    ordering: '',
                },
                options: [
                    {
                        label: '发布时间升序',
                        value: 'ascending'
                    },
                    {
                        label: '发布时间倒序',
                        value: 'descending'
                    }
                ],
                tableData: [
                    {
                        id: 1,
                        name: 'test-1',
                        creator: 'egg',
                        type: 'NONEEDLOGIN',
                        created_datetime: '2019',
                        ending_datetime: '2020'
                    },
                    {
                        id: 3,
                        name: 'admin-test',
                        creator: 'daty',
                        type: 'NONEEDLOGIN',
                        created_datetime: '2019',
                        ending_datetime: '2020',
                    }
                ],
                tableLoading: true,
                count: 1,
            }
        },
        mounted() {
            api.getCollectionListOrder().then(data => {
                this.options = data;
            });
            this.getOrUpdateCollectionList();
        },
        methods: {
            getOrUpdateCollectionList() {
                this.tableLoading = true;
                api.getCollectionList(this.params).then(data => {
                    this.tableData = data.results;
                    this.count = data.count;
                    this.tableLoading = false;
                });
            },
            clearSearch() {
                this.params.search = '';
            },
            sortChange(col) {
                //TODO
            },
            handleEdit(index, row) {
                this.$router.push({name: 'editCollection', params: {id: row.id}});
            },
            handleSubFile(index, row) {
                //TODO
            }
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
    .collection-list-wrap {
        width 100%
        height 100%

        .collection-list-menu {
            width 100%
            margin 0 auto
            height 40px
            margin-top 20px

            .el-col {
                padding-top 5px
                padding-bottom 5px

                .order {
                    width 100%
                }

                .search {
                    width 100%
                }

                .clearBtn {
                    width 100%
                }

                .addBtn {
                    width 100%
                }
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
