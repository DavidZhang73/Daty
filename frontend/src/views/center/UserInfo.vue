<template>
    <div class="user-info-wrap">
        <el-collapse class="user-info" accordion>
            <el-collapse-item name="1">
                <template slot="title">
                    <i class="el-icon-edit-outline"></i>&nbsp;修改姓名
                </template>
                <el-form :inline="true"
                         class="formItem"
                         :model="ruleFormName"
                         :rules="rulesName"
                         ref="ruleFormName">
                    <el-form-item label="新的姓名" prop="name">
                        <el-input
                                v-model.trim="ruleFormName.name"
                                placeholder="张某某"
                                auto-complete="name"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="onSubmitName">提交</el-button>
                    </el-form-item>
                </el-form>
            </el-collapse-item>
            <el-collapse-item name="2">
                <template slot="title">
                    <i class="el-icon-edit-outline"></i>&nbsp;修改手机号
                </template>
                <el-form :inline="true"
                         class="formItem"
                         :model="ruleFormPhonenumber"
                         :rules="rulesPhonenumber"
                         ref="ruleFormPhonenumber">
                    <el-form-item label="新的手机号" prop="phoneNumber">
                        <el-input
                                v-model.trim="ruleFormPhonenumber.phoneNumber"
                                placeholder="13088888888"
                                auto-complete="phoneNumber"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="onSubmitPhonenumber">提交</el-button>
                    </el-form-item>
                </el-form>
            </el-collapse-item>
            <el-collapse-item name="3">
                <template slot="title">
                    <i class="el-icon-edit-outline"></i>&nbsp;修改QQ
                </template>
                <el-form :inline="true"
                         class="formItem"
                         :model="ruleFormQQ"
                         :rules="rulesQQ"
                         ref="ruleFormQQ">
                    <el-form-item label="新的QQ" prop="QQ">
                        <el-input
                                v-model.trim="ruleFormQQ.QQ"
                                placeholder="12348888"
                                auto-complete="QQ"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="onSubmitQQ">提交</el-button>
                    </el-form-item>
                </el-form>
            </el-collapse-item>
        </el-collapse>
    </div>
</template>

<script>
    export default {
        name: "UserInfo",
        data() {
            var validateName = (rule, value, callback) => {
                //150个字符或者更少。包含字母，数字和仅有的@/./+/-/_符号。
                if (!value) {
                    return callback(new Error('请输入姓名'))
                } else if (value.length > 150) {
                    return callback(new Error('姓名应该小于150个字符'))
                }
                return callback()
            };
            var validatePhone = (rule, value, callback) => {
                let phoneRex = /^1[34578]\d{9}$/;
                if (!value) {
                    return callback()
                } else if (!phoneRex.test(value)) {
                    return callback(new Error('手机号格式不正确'))
                }
                return callback()
            };
            var validateQQ = (rule, value, callback) => {
                let qqRex = /[1-9][0-9]{4,}/;
                if (!value) {
                    return callback()
                } else if (!qqRex.test(value)) {
                    return callback(new Error('QQ格式不正确'))
                }
                return callback()
            };
            return {
                activeNames: ['1'],
                ruleFormName: {
                    name: ''
                },
                ruleFormPhonenumber: {
                    phoneNumber: ''
                },
                ruleFormQQ: {
                    QQ: ''
                },
                rulesName: {
                    name: [
                        {validator: validateName, trigger: 'blur'}
                    ],
                },
                rulesPhonenumber: {
                    phoneNumber: [
                        {validator: validatePhone, trigger: 'blur'}
                    ]
                },
                rulesQQ: {
                    QQ: [
                        {validator: validateQQ, trigger: 'blur'}
                    ]
                }
            }
        },
        methods: {
            onSubmitName() {

            },
            onSubmitPhonenumber() {

            },
            onSubmitQQ() {

            }
        }
    }
</script>

<style lang="stylus">
    .user-info-wrap {
        height 100%
        width 100%

        .user-info {
            height 100%
            width 100%

            .formItem {
                margin 0 auto

                .el-form-item {
                    margin 20px

                    .el-button {
                        margin-left -20px
                    }
                }
            }
        }
    }
</style>
