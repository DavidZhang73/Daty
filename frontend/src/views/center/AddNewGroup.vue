<template>
    <el-row class="addNewGroup-wrap">
        <el-col :xs="{span:24}"
                :sm="{span:20}"
                :lg="{span:16}">
            <el-form class="addNewGroup-form"
                     label-width="100px"
                     :model="addNewGroup">
                <el-form-item prop="userGroupName" label="用户组名称">
                    <el-input
                            type="text"
                            placeholder="请输入用户组名称"
                            v-model.trim="addNewGroup.userGroupName">
                    </el-input>
                </el-form-item>
                <el-form-item prop="userList" label="用户组成员">
                    <el-table :data="addNewGroup.userList">
                        <el-table-column label="#" type="index" align="center">
                        </el-table-column>
                        <el-table-column label="用户名称" align="center">
                            <template slot-scope="scope">
                                <template v-if="scope.row.edit">
                                    <el-input
                                            v-model.trim="scope.row.userName"
                                            size="small"></el-input>
                                </template>
                            </template>
                        </el-table-column>
                        <el-table-column label="操作" align="center">
                            <template slot-scope="scope"></template>
                        </el-table-column>
                    </el-table>
                    <el-button type="success"
                               plain>添加用户
                    </el-button>
                </el-form-item>
            </el-form>
        </el-col>
    </el-row>
</template>

<script>
    export default {
        name: "AddNewGroup",
        data() {
            return {
                addNewGroup: {
                    userGroupName: '',
                    userList: [],
                },
            }
        }
    }
</script>

<style lang="stylus">
    .addNewGroup-wrap {

        .addNewGroup-form {

            .el-input {
            }

            .el-form-item {

                .el-button {
                    width 100%
                    margin-top 10px
                }
            }
        }
    }
</style>