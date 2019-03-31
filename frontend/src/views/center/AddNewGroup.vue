<template>
    <el-row class="addNewGroup-wrap">
        <el-col :xs="{span:24}"
                :sm="{span:20}"
                :lg="{span:16}">
            <div class="selectLoginModel">
                <el-radio v-model="radio" :label="radioOptions[0].label">{{radioOptions[0].name}}</el-radio>
                <el-radio v-model="radio" :label="radioOptions[1].label">{{radioOptions[1].name}}</el-radio>
                <el-radio v-model="radio" :label="radioOptions[2].label">{{radioOptions[2].name}}</el-radio>
            </div>

            <el-form class="addNewGroupForm-NONEEDLOGIN"
                     label-width="100px"
                     :model="userGroupInfo"
                     label-position="left"
                     v-if="showNONEEDLOGINForm">
                <el-form-item prop="userGroupName" label="用户组名称">
                    <el-input
                            type="text"
                            placeholder="请输入用户组名称"
                            v-model.trim="userGroupInfo.userGroupName">
                    </el-input>
                </el-form-item>
                <el-form-item prop="userList" label="用户组成员">
                    <el-table :data="userGroupInfo.userList">
                        <el-table-column label="#" type="index" align="center">
                        </el-table-column>
                        <el-table-column label="用户名称" align="center">
                            <template slot-scope="scope">
                                <span style="margin-left: 10px">{{ scope.row.name }}</span>
                            </template>
                        </el-table-column>
                        <el-table-column label="操作" align="center">

                        </el-table-column>
                    </el-table>
                    <el-button class="addNewGroupBtn"
                               icon="el-icon-circle-plus-outline"
                               type="success"
                               @click="handleAddUser"
                               plain>添加用户
                    </el-button>
                </el-form-item>
            </el-form>
        </el-col>
        <el-col :xs="{span:24}"
                :sm="{span:20}"
                :lg="{span:16}"
                v-if="showAddForm">
            <el-card class="box-card">
                <el-form :model="addNewUser" label-width="100px" label-position="left" class="addNewUser-form">
                    <el-form-item label="用户名">
                        <el-input type="text" placeholder="请输入用户组名称" v-model="addNewUser.userName"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-button class="addBtn" type="primary" plain @click="submitAddNewUserForm">添加</el-button>
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
            return {
                radio: 'NONEEDLOGIN',
                userGroupInfo: {
                    userGroupName: '',
                    userList: [],
                },
                showAddForm: false,
                addNewUser: {
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
            }
        },
        mounted() {
            api.getUserGroupType().then(data => {
                for (var i = 0; i < data.length; i++) {
                    this.radioOptions[i].label = data[i].value;
                    this.radioOptions[i].name = data[i].label;
                }
            });
        },
        methods: {
            submitAddNewUserForm() {
                var userMap = [];
                userMap["name"] = this.addNewUser.userName;
                this.userGroupInfo.userList.push(userMap);
                this.addNewUser.userName = '';
            },
            handleAddUser() {
                this.showAddForm = !this.showAddForm;
            },
        },
        watch: {
            radio(newVal) {
                if (newVal === "ALREADYSIGNIN") {
                    this.showNONEEDLOGINForm = false;
                    this.showALREADYSIGNINForm = true;
                    this.showREQUIRESIGNINForm = false;
                } else if (newVal === "REQUIRESIGNIN") {
                    this.showNONEEDLOGINForm = false;
                    this.showALREADYSIGNINForm = false;
                    this.showREQUIRESIGNINForm = true;
                } else {
                    this.showNONEEDLOGINForm = true;
                    this.showALREADYSIGNINForm = false;
                    this.showREQUIRESIGNINForm = false;
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

                .addNewGroupBtn {
                    width 100%
                    margin-top 10px
                }
            }
        }

        .addNewUser-form {

            .addBtn {
                float right
                right 0
            }
        }
    }
</style>