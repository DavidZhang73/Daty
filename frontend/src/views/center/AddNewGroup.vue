<template>
    <el-row class="addNewGroup-wrap">
        <el-col :xs="{span:24}"
                :sm="{span:20}"
                :lg="{span:16}">
            <el-form class="addNewGroup-form" label-width="100px">
                <el-form-item prop="userGroupName" label="用户组名称">
                    <el-input
                            type="text"
                            placeholder="请输入用户组名称">
                    </el-input>
                </el-form-item>
                <el-form-item prop="userList" label="用户组成员">

                </el-form-item>
            </el-form>
        </el-col>
    </el-row>
</template>

<script>
    export default {
        name: "AddNewGroup"
    }
</script>

<style lang="stylus">
    .addNewGroup-wrap {

        .addNewGroup-form {

            .el-input {
            }
        }
    }
</style>