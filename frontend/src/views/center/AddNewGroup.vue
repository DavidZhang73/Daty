<template>
    <el-row class="addNewGroup-wrap"
            v-loading="addNewGroupLoading"
            element-loading-text="拼命加载中"
            element-loading-spinner="el-icon-loading"
            element-loading-background="rgba(0, 0, 0, 0.8)">
        <el-col :xs="{span:24}"
                :sm="{span:20}"
                :lg="{span:16}">
            <div class="selectLoginModel">
                <el-radio v-model="radio" :label="radioOptions[0].label">{{radioOptions[0].name}}</el-radio>
                <el-radio v-model="radio" :label="radioOptions[1].label" disabled>{{radioOptions[1].name}}</el-radio>
                <el-radio v-model="radio" :label="radioOptions[2].label" disabled>{{radioOptions[2].name}}</el-radio>
            </div>

            <el-form class="addNewGroupForm-NONEEDLOGIN"
                     label-width="100px"
                     :model="userGroupInfoNONEEDLOGIN"
                     ref="userGroupInfoNONEEDLOGIN"
                     :rules="userGroupInfoRulesNONEEDLOGIN"
                     status-icon
                     label-position="left"
                     v-if="showNONEEDLOGINForm">
                <el-form-item prop="userGroupName" label="用户组名称">
                    <el-input
                            type="text"
                            placeholder="请输入用户组名称"
                            v-model.trim="userGroupInfoNONEEDLOGIN.userGroupName">
                    </el-input>
                </el-form-item>
                <el-form-item prop="userList" label="用户组成员">
                    <el-table :data="userGroupInfoNONEEDLOGIN.userList">
                        <el-table-column label="#" type="index" align="center">
                        </el-table-column>
                        <el-table-column label="用户名称" align="center">
                            <template slot-scope="scope">
                                <span style="margin-left: 10px">{{ scope.row.name }}</span>
                            </template>
                        </el-table-column>
                        <el-table-column label="操作" align="center">
                            <template slot-scope="scope">
                                <el-button
                                        size="mini"
                                        type="danger"
                                        @click="handleDeleteInNONEEDLOGIN(scope.$index, scope.row)"
                                        plain>删除
                                </el-button>
                            </template>
                        </el-table-column>
                    </el-table>
                    <el-button class="addNewGroupBtn"
                               icon="el-icon-circle-plus-outline"
                               type="success"
                               @click="handleAddUserForNONEEDLOGIN"
                               size="mini"
                               plain>添加用户
                    </el-button>
                </el-form-item>
                <el-form-item>
                    <el-button
                            class="submitGroupListBtn"
                            type="primary"
                            v-if="!showAddFormNONEEDLOGIN"
                            icon="el-icon-check"
                            size="small"
                            @click="submitGroupListNONEEDLOGIN('userGroupInfoNONEEDLOGIN')">保存
                    </el-button>
                </el-form-item>
            </el-form>

            <el-form v-if="showALREADYSIGNINForm">
                <el-form-item label="showALREADYSIGNINForm"></el-form-item>
            </el-form>

            <el-form v-if="showREQUIRESIGNINForm">
                <el-form-item label="showREQUIRESIGNINForm"></el-form-item>
            </el-form>
        </el-col>
        <el-col :xs="{span:24}"
                :sm="{span:20}"
                :lg="{span:16}"
                v-if="showAddFormNONEEDLOGIN">
            <el-card class="box-card">
                <el-form
                        :model="addNewUserNONEEDLOGIN"
                        label-width="100px"
                        label-position="left"
                        class="addNewUser-form"
                        ref="addNewUserNONEEDLOGIN"
                        :rules="addNewUserRulesNONEEDLOGIN">
                    <el-form-item label="用户名" prop="userName">
                        <el-input
                                type="text"
                                placeholder="请输入用户名称"
                                v-model="addNewUserNONEEDLOGIN.userName"
                                @keypress.enter.native="submitAddNewUserFormForNONEEDLOGIN('addNewUserNONEEDLOGIN')"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <div class="btnGroup">
                            <el-button
                                    class="addBtn"
                                    type="primary"
                                    size="small"
                                    plain
                                    @click="submitAddNewUserFormForNONEEDLOGIN('addNewUserNONEEDLOGIN')">添加
                            </el-button>
                            <el-button
                                    class="cancelBtn"
                                    type="danger"
                                    size="small"
                                    plain
                                    @click="cancelAddInNONEEDLOGIN">取消
                            </el-button>
                        </div>
                    </el-form-item>
                </el-form>
            </el-card>
        </el-col>
    </el-row>
</template>

<script>
    import api from '../../api'

    export default {
        name: "AddNewGroup",
        data() {
            var validateUserGroupNameNONEEDLOGIN = (rule, value, callback) => {
                if (!value) {
                    return callback(new Error('用户组名称不可为空'))
                } else if (value.length > 150) {
                    return callback(new Error('用户组名称应该小于150个字符'))
                }
                return callback()
            };
            var validateUserNameNONEEDLOGIN = (rule, value, callback) => {
                if (!value) {
                    return callback(new Error('用户名称不可为空'))
                } else if (value.length > 150) {
                    return callback(new Error('用户名称应该小于150个字符'))
                }
                return callback()
            };
            return {
                addNewGroupLoading: true,
                radio: 'NONEEDLOGIN',
                userGroupInfoNONEEDLOGIN: {
                    userGroupName: '',
                    userList: [],
                },
                showAddFormNONEEDLOGIN: false,
                addNewUserNONEEDLOGIN: {
                    userName: '',
                },
                radioOptions: [
                    {
                        label: '',
                        name: ''
                    },
                    {
                        label: '',
                        name: ''
                    },
                    {
                        label: '',
                        name: ''
                    }
                ],
                showNONEEDLOGINForm: true,
                showALREADYSIGNINForm: false,
                showREQUIRESIGNINForm: false,
                userGroupInfoRulesNONEEDLOGIN: {
                    userGroupName: [
                        {validator: validateUserGroupNameNONEEDLOGIN, trigger: 'blur'}
                    ],
                },
                addNewUserRulesNONEEDLOGIN: {
                    userName: [
                        {validator: validateUserNameNONEEDLOGIN, trigger: 'blur'}
                    ],
                },
            }
        },
        mounted() {
            this.addNewGroupLoading = true;
            api.getUserGroupType().then(data => {
                for (var i = 0; i < data.length; i++) {
                    this.radioOptions[i].label = data[i].value;
                    this.radioOptions[i].name = data[i].label;
                }
                this.addNewGroupLoading = false;
            });
        },
        methods: {
            submitAddNewUserFormForNONEEDLOGIN(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        var userMap = [];
                        userMap["name"] = this.addNewUserNONEEDLOGIN.userName;
                        this.userGroupInfoNONEEDLOGIN.userList.push(userMap);
                        this.addNewUserNONEEDLOGIN.userName = '';
                    } else return false;
                });
            },
            handleAddUserForNONEEDLOGIN() {
                this.showAddFormNONEEDLOGIN = !this.showAddFormNONEEDLOGIN;
            },
            submitGroupListNONEEDLOGIN(formName) {


                //TODO
            },
            cancelAddInNONEEDLOGIN() {
                this.showAddFormNONEEDLOGIN = false;
            },
            handleDeleteInNONEEDLOGIN(index) {
                this.userGroupInfoNONEEDLOGIN.userList.splice(index, 1);
            },
        },
        watch: {
            radio(newVal) {
                if (newVal === "ALREADYSIGNIN") {
                    this.showNONEEDLOGINForm = false;
                    this.showALREADYSIGNINForm = true;
                    this.showREQUIRESIGNINForm = false;
                    if (this.showAddFormNONEEDLOGIN) this.showAddFormNONEEDLOGIN = false;
                } else if (newVal === "REQUIRESIGNIN") {
                    this.showNONEEDLOGINForm = false;
                    this.showALREADYSIGNINForm = false;
                    this.showREQUIRESIGNINForm = true;
                    if (this.showAddFormNONEEDLOGIN) this.showAddFormNONEEDLOGIN = false;
                } else {
                    this.showNONEEDLOGINForm = true;
                    this.showALREADYSIGNINForm = false;
                    this.showREQUIRESIGNINForm = false;
                    if (this.showAddFormNONEEDLOGIN) this.showAddFormNONEEDLOGIN = false;
                }
            }
        }
    }
</script>

<style lang="stylus">
    .addNewGroup-wrap {
        .selectLoginModel {
            margin-top 20px
            margin-bottom 30px
        }

        .addNewGroupForm-NONEEDLOGIN {

            .el-input {
            }

            .el-form-item {
                margin-bottom 15px

                .submitGroupListBtn {
                    float right
                    right 0
                }

                .addNewGroupBtn {
                    width 100%
                    margin-top 10px
                }
            }
        }

        .box-card {
            margin-left 100px

            .el-card__body {
                padding 10px 20px 5px 20px

                .addNewUser-form {

                    .el-form-item {
                        margin-bottom 5px

                        .btnGroup {
                            float right
                            right 0
                        }
                    }
                }
            }
        }
    }
</style>