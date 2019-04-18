<template>
    <el-row class="editUserGroup-wrap"
            v-loading="Loading"
            element-loading-text="拼命加载中"
            element-loading-spinner="el-icon-loading"
            element-loading-background="rgba(255, 255, 255, 1)">
        <el-col :xs="{span:24}"
                :sm="{span:20}"
                :lg="{span:18}">
            <el-form class="userGroupForm"
                     :model="userGroupForm"
                     ref="userGroupForm"
                     :rules="userGroupFormRules"
                     label-position="left"
                     label-width="100px"
                     status-icon>
                <el-form-item prop="type" label="用户组类型">
                    <el-radio-group v-model="userGroupForm.type" disabled>
                        <el-radio v-for="item in radioOptions"
                                  :label="item.value">{{item.label}}
                        </el-radio>
                    </el-radio-group>
                </el-form-item>
                <el-form-item label="用户组名称" prop="name">
                    <el-input v-model.trim="userGroupForm.name" placeholder="请输入用户组名称"></el-input>
                </el-form-item>
                <el-form-item label="用户列表" prop="users">
                    <el-table :data="userGroupForm.users"
                              v-if="userGroupForm.type === 'NONEEDLOGIN'"
                              height="400">
                        <el-table-column type="index" label="#" align="center"></el-table-column>
                        <el-table-column label="用户名称" align="center">
                            <template slot-scope="scope">
                                <span>{{scope.row.name}}</span>
                            </template>
                        </el-table-column>
                        <el-table-column label="操作" align="center">
                            <template slot-scope="scope">
                                <el-button
                                        size="mini"
                                        type="danger"
                                        @click="handleDelete(scope.$index, scope.row)"
                                        plain>删除
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
                    <div class="btnGroup"
                         v-if="!(showAddNoNeedLoginUserForm||showAddAlreadySignInUserForm||showAddRequireSignInUserForm)">
                        <el-button
                                type="primary"
                                class="submitBtn"
                                @click="submitUserGroupForm('userGroupForm')">保存
                        </el-button>
                        <el-button
                                type="danger"
                                class="deleteBtn"
                                @click="deleteForm">删除
                        </el-button>
                    </div>
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
        name: "EditUserGroup",
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
                userGroupForm: {},
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
            handleDelete(index) {
                this.userGroupForm.users.splice(index, 1);
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
                        api.updateUserGroupById(
                            this.$route.params.id,
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
            deleteForm() {
                this.$confirm('此操作将永久删除该用户组, 是否继续?', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    api.deleteUserGroup(
                        this.$route.params.id
                    );
                    this.Loading = false;
                    this.$router.push({name: 'groupList'});
                    this.$message({
                        type: 'success',
                        message: '删除成功!'
                    });
                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '已取消删除'
                    });
                });
            }
        },
        mounted() {
            this.Loading = true;
            api.getUserGroupById(this.$route.params, this.$route.params.id).then(data => {
                this.userGroupForm = data;
                this.Loading = false;
            });
            api.getUserGroupType().then(data => {
                this.radioOptions = data;
            })
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
    .editUserGroup-wrap {
        width 100%

        .userGroupForm {
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

                .btnGroup {
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