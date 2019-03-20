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
                    </el-button>
                </el-input>

                <el-button
                        class="clearBtn"
                        icon="el-icon-delete"
                        @click="clearTypeAndSearch();getOrUpdateGroupInfo();">清空搜索
                </el-button>
            </div>

            <div class="group-list-menu-right">
                <el-button
                        class="add-btn"
                        icon="el-icon-plus"
                        type="primary"
                        @click="addNewGroup()">
                    新建用户组
                </el-button>
            </div>
        </div>

        <el-table :data="tableData">
            <el-table-column
                    label="序号"
                    type="index">
            </el-table-column>
            <el-table-column
                    label="用户组名称"
                    width="90px">
                <template slot-scope="scope">
                    <span style="margin-left: 10px">{{ scope.row.name }}</span>
                </template>
            </el-table-column>
            <el-table-column
                    label="人数"
                    width="60px">
                <template slot-scope="scope">
                    <span style="margin-left: 10px">{{ scope.row.users_count }}</span>
                </template>
            </el-table-column>
            <el-table-column
                    label="类别"
                    width="145px">
                <template slot-scope="scope">
                    <span style="margin-left: 10px">{{ scope.row.type }}</span>
                </template>
            </el-table-column>
            <el-table-column
                    label="创建日期">
                <template slot-scope="scope">
                    <i class="el-icon-time"></i>
                    <span style="margin-left: 10px">{{ scope.row.created_datetime }}</span>
                </template>
            </el-table-column>
            <el-table-column
                    label="上次修改日期">
                <template slot-scope="scope">
                    <i class="el-icon-time"></i>
                    <span style="margin-left: 10px">{{ scope.row.last_modified_datetime }}</span>
                </template>
            </el-table-column>
            <el-table-column label="操作">
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
                layout="prev, pager, next, jumper"
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
            }
        },
        mounted() {
            api.getUserGroupType().then(data => {
                this.options = data;
            });
            this.getOrUpdateGroupInfo()
        },
        methods: {
            addNewGroup() {
                console.log('addNewGroup');
                //TODO

            },
            handleEdit(index, row) {
                console.log(index, row);
                //TODO
            },
            getOrUpdateGroupInfo() {
                api.getUserGroup(this.params).then(data => {
                    for (var i = 0; i < data.results.length; i++) {
                        if (data.results[i].type === 'NONEEDLOGIN') data.results[i].type = '不需要登陆';
                        else if (data.results[i].type === 'ALREADYSIGNIN') data.results[i].type = '需要登陆已注册';
                        else data.results[i].type = '需要登陆未注册';

                        var tempStr1 = data.results[i].created_datetime;
                        data.results[i].created_datetime = tempStr1.substring(0, 10) + " " + tempStr1.substring(11, 19);

                        var tempStr2 = data.results[i].last_modified_datetime;
                        data.results[i].last_modified_datetime = tempStr2.substring(0, 10) + " " + tempStr2.substring(11, 19);
                    }

                    this.tableData = data.results;
                    this.count = data.count;
                });
            },
            clearTypeAndSearch() {
                this.params.search = '';
            }
        }
    }
</script>

<style lang="stylus">
    .group-list-wrap {
        width 100%
        height 100%

        .group-list-menu {
            width 70%
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
                    width 200px
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
            width 70%
        }

        .el-pagination {
            margin 0 auto
            width 70%
            margin-top 40px
            margin-bottom 20px
        }
    }
</style>
