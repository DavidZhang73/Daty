<template>
    <el-row class="collection-list-wrap">
        <el-col :xs="{span:24}"
                :sm="{span:24}"
                :lg="{span:20,offset:2}">
            <div class="collection-list-menu">
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
                <el-input class="search" placeholder="搜索..." v-model="params.search">
                    <el-button slot="append"
                               icon="el-icon-search"
                               @click="getOrUpdateCollectionList()">
                        搜索
                    </el-button>
                </el-input>
                <el-button
                        class="clearBtn"
                        icon="el-icon-delete"
                        @click="clearSearch();getOrUpdateCollectionList();">清空搜索
                </el-button>
                <router-link :to="{name : 'addNewCollection'}">
                    <el-button
                            class="addBtn"
                            icon="el-icon-plus"
                            type="primary">
                        新建文件集
                    </el-button>
                </router-link>
            </div>

            <el-table :data="tableData"
                      @sort-change="sortChange"
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
                tableData: [],
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
