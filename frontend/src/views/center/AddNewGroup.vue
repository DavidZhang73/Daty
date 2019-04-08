<template>
    <el-row class="addNewGroup-wrap"
            v-loading="Loading"
            element-loading-text="拼命加载中"
            element-loading-spinner="el-icon-loading"
            element-loading-background="rgba(0, 0, 0, 0.8)">
        <el-col :xs="{span:24}"
                :sm="{span:20}"
                :lg="{span:18}">
            <el-form class="addNewGroupForm"
                     :model="userGroupForm"
                     ref="userGroupForm"
                     label-position="left"
                     label-width="100px"
                     :rules="userGroupFormRules"
                     status-icon>
                <el-form-item label="用户类型" prop="type">
                    <el-radio-group v-model="userGroupForm.type"
                                    @change="handleChange">
                        <el-radio v-for="item in radioOptions"
                                  :label="item.value">{{item.label}}
                        </el-radio>
                    </el-radio-group>
                </el-form-item>
                <el-form-item label="用户组名称" prop="name">
                    <el-input v-model.trim="userGroupForm.name" placeholder="请输入用户组名称"></el-input>
                </el-form-item>
                <el-form-item label="用户列表" prop="users">
                    <el-table :data="userGroupForm.users" v-if="userGroupForm.type === 'NONEEDLOGIN'">
                        <el-table-column type="index" align="center"></el-table-column>
                        <el-table-column label="用户名称" align="center" prop="name"></el-table-column>
                        <el-table-column label="操作" align="center">
                            <template slot-scope="scope">
                                <el-button
                                        size="mini"
                                        type="danger"
                                        @click="handleDelete(scope.$index, scope.row)">删除
                                </el-button>
                            </template>
                        </el-table-column>
                    </el-table>

                    <el-table :data="userGroupForm.users" v-if="userGroupForm.type === 'ALREADYSIGNIN'">
                        <el-table-column type="index" label="#" align="center"></el-table-column>
                        <el-table-column label="用户" align="center"></el-table-column>
                        <el-table-column label="操作" align="center"></el-table-column>
                    </el-table>

                    <el-table :data="userGroupForm.users" v-if="userGroupForm.type === 'REQUIRESIGNIN'">
                        <el-table-column type="index" label="#" align="center"></el-table-column>
                        <el-table-column label="用户" align="center"></el-table-column>
                        <el-table-column label="操作" align="center"></el-table-column>
                    </el-table>

                    <el-button class="addBtn"
                               type="success"
                               icon="el-icon-circle-plus-outline"
                               size="mini"
                               @click="addNewUser"
                               plain>添加用户
                    </el-button>
                </el-form-item>
                <el-form-item>
                    <el-button
                            type="primary"
                            class="submitBtn"
                            v-if="!(showAddNoNeedLoginUserForm||showAddAlreadySignInUserForm||showAddRequireSignInUserForm)"
                            @click="submitUserGroupForm('userGroupForm')">保存
                    </el-button>
                </el-form-item>
            </el-form>

            <el-card class="addNoNeedLoginUser" v-if="showAddNoNeedLoginUserForm">
                <el-form :model="NoNeedLoginUserForm"
                         ref="NoNeedLoginUserForm"
                         :rules="NoNeedLoginUserFormRules"
                         label-position="left"
                         label-width="100px"
                         status-icon>
                    <el-form-item label="用户名称" prop="name">
                        <el-input
                                v-model.trim="NoNeedLoginUserForm.name"
                                placeholder="请输入用户名"
                                @keypress.enter.native="submitNewNoNeedLoginUser('NoNeedLoginUserForm')"
                                clearable></el-input>
                    </el-form-item>
                    <el-form-item class="btnGroup">
                        <el-button type="primary" size="mini" @click="submitNewNoNeedLoginUser('NoNeedLoginUserForm')"
                                   plain>添加
                        </el-button>
                        <el-button type="danger" size="mini" @click="cancelAddNoNeedLoginUser" plain>取消</el-button>
                    </el-form-item>
                </el-form>
            </el-card>

            <el-card class="addAlreadySignInUser" v-if="showAddAlreadySignInUserForm">
                <p>TEST-01</p>
            </el-card>

            <el-card class="addRequireSignInUser" v-if="showAddRequireSignInUserForm">
                <p>TEST-02</p>
            </el-card>
        </el-col>
    </el-row>
</template>

<script>
    import api from '../../api'

    export default {
        name: "AddNewGroup",
        data() {
            var validateUsername = (rule, value, callback) => {
                if (!value) {
                    return callback(new Error('用户名称不可为空'))
                } else if (value.length > 128) {
                    return callback(new Error('用户名称应该小于128个字符'))
                }
                return callback()
            };
            var validateUserGroupName = (rule, value, callback) => {
                if (!value) {
                    return callback(new Error('用户组名称不可为空'))
                } else if (value.length > 128) {
                    return callback(new Error('用户组名称应该小于128个字符'))
                }
                return callback()
            };
            var validateUsers = (rule, value, callback) => {
                if (value.length === 0) {
                    return callback(new Error('用户列表不能为空'))
                }
                return callback()
            };
            return {
                Loading: true,
                userGroupForm: {
                    type: 'NONEEDLOGIN',
                    name: '',
                    users: [],
                },
                userGroupFormRules: {
                    name: [
                        {validator: validateUserGroupName, trigger: 'blur'}
                    ],
                    users: [
                        {validator: validateUsers, trigger: 'blur'}
                    ]
                },
                radioOptions: [],

                NoNeedLoginUserForm: {
                    name: '',
                },
                NoNeedLoginUserFormRules: {
                    name: [
                        {validator: validateUsername, trigger: 'blur'}
                    ]
                },
                showAddNoNeedLoginUserForm: false,

                AlreadySignInUserForm: {
                    name: '',
                },
                AlreadySignInUserFormRules: {},
                showAddAlreadySignInUserForm: false,

                RequireSignInInUserForm: {
                    name: '',
                },
                RequireSignInUserFormRules: {},
                showAddRequireSignInUserForm: false,

            }
        },
        methods: {
            handleChange() {
                this.NoNeedLoginUserForm.name = '';
                this.AlreadySignInUserForm.name = '';
                this.RequireSignInInUserForm.name = '';
                this.showAddNoNeedLoginUserForm = false;
                this.showAddAlreadySignInUserForm = false;
                this.showAddRequireSignInUserForm = false;
            },
            addNewUser() {
                if (this.userGroupForm.type === 'ALREADYSIGNIN') {
                    this.showAddNoNeedLoginUserForm = false;
                    this.showAddAlreadySignInUserForm = true;
                    this.showAddRequireSignInUserForm = false;
                } else if (this.userGroupForm.type === 'REQUIRESIGNIN') {
                    this.showAddNoNeedLoginUserForm = false;
                    this.showAddAlreadySignInUserForm = false;
                    this.showAddRequireSignInUserForm = true;
                } else {
                    this.showAddNoNeedLoginUserForm = true;
                    this.showAddAlreadySignInUserForm = false;
                    this.showAddRequireSignInUserForm = false;
                }
            },
            submitNewNoNeedLoginUser(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        this.userGroupForm.users = JSON.parse(JSON.stringify(this.userGroupForm.users.concat(this.NoNeedLoginUserForm)));
                        this.NoNeedLoginUserForm.name = '';
                    } else return false;
                });
            },
            cancelAddNoNeedLoginUser() {
                this.NoNeedLoginUserForm.name = '';
                this.showAddNoNeedLoginUserForm = false;
            },
            submitUserGroupForm(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        this.Loading = true;
                        api.updateUserGroup(
                            this.userGroupForm.name,
                            this.userGroupForm.type,
                            this.userGroupForm.users
                        ).then(data => {
                            if (data.error) {
                                this.Loading = false;
                                this.$message.error({showClose: true, message: data.error});
                            } else {
                                this.Loading = false;
                                this.$router.push({name: 'groupList'});
                            }
                        })
                    } else return false;
                })
            },
            handleDelete(index) {
                this.userGroupForm.users.splice(index, 1);
            }
        },
        mounted() {
            this.Loading = true;
            api.getUserGroupType().then(data => {
                this.radioOptions = data;
                this.Loading = false;
            })
        }
    }
</script>

<style lang="stylus">
    .addNewGroup-wrap {
        width 100%

        .addNewGroupForm {
            width 100%

            .el-form-item {
                width 100%

                .el-table {
                    width 100%
                }

                .addBtn {
                    width 100%
                    margin-top 10px
                }

                .submitBtn {
                    float right
                    right 0
                }
            }
        }

        .addNoNeedLoginUser {
            margin-left 100px

            .el-card__body {
                padding-bottom 0

                .btnGroup {
                    float right
                    right 0
                }
            }
        }
    }
</style>