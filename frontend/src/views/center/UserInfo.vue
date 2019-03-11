<template>
    <div class="user-info-wrap">
        <el-form class="user-info-form"
                 :model="infoForm"
                 :rules="rules"
                 ref="infoForm"
                 status-icon>
            <el-form-item prop="name">
                <el-input
                        type="text"
                        v-model.trim="infoForm.name"
                        :placeholder="oldName">
                    <template slot="prepend">新的姓名</template>
                </el-input>
            </el-form-item>
            <el-form-item prop="phoneNumber">
                <el-input
                        type="text"
                        v-model.trim="infoForm.phoneNumber"
                        :placeholder="oldPhone">
                    <template slot="prepend">新的手机号</template>
                </el-input>
            </el-form-item>
            <el-form-item prop="QQ">
                <el-input
                        type="text"
                        v-model.trim="infoForm.QQ"
                        :placeholder="oldQQ">
                    <template slot="prepend">新的QQ</template>
                </el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="submitForm('infoForm')">保存修改</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
    export default {
        name: "UserInfo",
        data() {
            var validateUsername = (rule, value, callback) => {
                //150个字符或者更少。包含字母，数字和仅有的@/./+/-/_符号。
                if (!value) {
                    return callback()
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
                oldName: '',
                oldPhone: '',
                oldQQ: '',
                infoForm: {
                    name: '',
                    phoneNumber: '',
                    QQ: '',
                },
                rules: {
                    name: [
                        {validator: validateUsername, trigger: 'blur'}
                    ],
                    phoneNumber: [
                        {validator: validatePhone, trigger: 'blur'}
                    ],
                    QQ: [
                        {validator: validateQQ, trigger: 'blur'}
                    ],
                },
            };
        },
        methods: {
            submitForm(formName) {

            }
        }
    }
</script>

<style lang="stylus">
    .user-info-wrap {
        margin-top 50px
        height 100%
        width 100%

        .el-form {
            width 70%
            height 100%
            margin 0 auto

            .el-form-item {

                .el-input-group__prepend {
                    text-align center
                    width 80px
                }

                .el-button {
                    float right
                    right 0
                }
            }
        }
    }
</style>
