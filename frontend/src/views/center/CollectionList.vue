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
                      v-loading="tableLoading"
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
                        {{scope.row.creator.username}}
                    </template>
                </el-table-column>
                <el-table-column
                        label="开始日期"
                        prop="start_datetime"
                        align="center">
                    <template slot-scope="scope">
                        <i class="el-icon-time"></i>
                        <span>
                        {{ scope.row.start_datetime}}</span>
                    </template>
                </el-table-column>
                <el-table-column
                        label="截至日期"
                        prop="end_datetime"
                        align="center">
                    <template slot-scope="scope">
                        <i class="el-icon-time"></i>
                        <span>
                        {{ scope.row.end_datetime}}</span>
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
                                v-if="scope.row.creator.id === $store.state.user.id">
                            编辑
                        </el-button>
                        <el-button
                                style="margin-left: 3px;"
                                type="primary"
                                size="mini"
                                @click="handleSubFile(scope.$index, scope.row)">
                            提交/下载
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
                        value: 'create_datetime'
                    },
                    {
                        label: '发布时间倒序',
                        value: '-create_datetime'
                    }
                ],
                tableData: [],
                tableLoading: true,
                count: 1,
            }
        },
        mounted() {
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
            handleEdit(index, row) {
                this.$router.push({name: 'editCollection', params: {id: row.id}});
            },
            handleSubFile(index, row) {
                this.$router.push({name: 'fileUploadAndDownload', params: {id: row.id}});
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
