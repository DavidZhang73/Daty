<template>
    <div class="user-info-wrap">
        <el-form class="user-info-form"
                 :model="infoForm"
                 :rules="rules"
                 ref="infoForm"
                 status-icon
                 v-if="showForm"
                 :label-position="labelPosition"
                 label-width="50px">
            <el-form-item prop="email" label="邮箱">
                <el-input
                        type="text"
                        v-model.trim="infoForm.email"
                        disabled>
                </el-input>
            </el-form-item>
            <el-form-item prop="name" label="姓名">
                <el-input
                        type="text"
                        v-model.trim="infoForm.name">
                </el-input>
            </el-form-item>
            <el-form-item prop="phoneNumber" label="手机">
                <el-input
                        type="text"
                        v-model.trim="infoForm.phoneNumber">
                </el-input>
            </el-form-item>
            <el-form-item prop="QQ" label="QQ">
                <el-input
                        type="text"
                        v-model.trim="infoForm.QQ"
                        @keypress.enter.native="submitForm('infoForm')">
                </el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="submitForm('infoForm')">保存修改</el-button>
            </el-form-item>
        </el-form>

        <div class="feedback-success" v-if="showFeedbackSuccess">
            <div class="icon-success">
                <i class="el-icon-circle-check-outline"></i>
                <p class="infoText">修改成功</p>
            </div>
            <p class="returnText">{{ timerTextSuccess }}</p>
        </div>

        <div class="feedback-error" v-if="showFeedbackError">
            <div class="icon-error">
                <i class="el-icon-circle-close-outline"></i>
                <p class="infoText">修改失败</p>
            </div>
            <p class="returnText">{{ timerTextError }}</p>
        </div>
    </div>
</template>

<script>
    import api from '../../api'

    export default {
        name: "UserInfo",
        data() {
            var validateUsername = (rule, value, callback) => {
                //150个字符或者更少。包含字母，数字和仅有的@/./+/-/_符号。
                if (!value) {
                    return callback(new Error('姓名不可为空'))
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
                labelPosition: 'left',
                showForm: true,
                showFeedbackSuccess: false,
                showFeedbackError: false,
                autoTime: 5,
                timerTextSuccess: '5秒后返回',
                timerTextError: '5秒后返回',
                infoForm: {
                    email: '',
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
        mounted() {
            api.getUserInfo().then(data => {
                if (data.error) {
                    this.$message.error({showClose: true, message: data.error});
                } else {
                    this.infoForm.email = data.data.email;
                    this.infoForm.name = data.data.username;
                    this.infoForm.phoneNumber = data.data.phone;
                    this.infoForm.QQ = data.data.qq;
                }
            })
        },
        methods: {
            submitForm(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        api.updateUserInfo(
                            this.infoForm.name,
                            this.infoForm.phoneNumber,
                            this.infoForm.QQ,
                        ).then(data => {
                            if (data.error) {
                                this.changeError();
                            } else {
                                let user = {
                                    id: this.$store.state.user.id,
                                    username: data.data.username,
                                };
                                this.$store.dispatch('userLogin', user);
                                this.changeSuccess();
                            }
                        })
                    } else return false;
                });
            },
            changeSuccess() {
                this.showForm = false;
                this.showFeedbackSuccess = true;
                this.showFeedbackError = false;
                this.autoTime = 5;
                this.userInfoTimerSuccess();
            },
            changeError() {
                this.showForm = false;
                this.showFeedbackSuccess = false;
                this.showFeedbackError = true;
                this.autoTime = 5;
                this.userInfoTimerError();
            },
            userInfoTimerSuccess() {
                let timer = setInterval(() => {
                    this.autoTime--;
                    this.timerTextSuccess = this.autoTime + '秒后返回';
                    if (this.autoTime <= 0) {
                        this.showForm = true;
                        this.showFeedbackSuccess = false;
                        this.showFeedbackError = false;
                        clearInterval(timer);
                    }
                }, 1000);
            },
            userInfoTimerError() {
                let timer = setInterval(() => {
                    this.autoTime--;
                    this.timerTextError = this.autoTime + '秒后返回';
                    if (this.autoTime <= 0) {
                        this.showForm = true;
                        this.showFeedbackSuccess = false;
                        this.showFeedbackError = false;
                        clearInterval(timer);
                    }
                }, 1000);
            },
        },
    }
</script>

<style lang="stylus">
    .user-info-wrap {
        margin-top 50px
        height 100%
        width 100%

        .el-form {
            width 60%
            height 100%
            margin-left 60px

            .el-form-item {

                .el-button {
                    float right
                    right 0
                }
            }
        }

        .feedback-success {
            width 100%
            height 100%
            margin 0 auto

            .icon-success {
                width 80px
                height 100%
                margin 0 auto

                i {
                    font-size 80px
                    color #67C23A

                    height 100%
                    margin 0 auto
                }

                .infoText {
                    font-size 18px
                    color #67C23A
                    text-align center

                    height 100%
                    margin 0 auto
                }
            }

            .returnText {
                padding-top 10px
                font-size 12px
                color rgb(105, 105, 105)
                text-align center

                height 100%
                margin 0 auto
            }
        }

        .feedback-error {
            width 100%
            height 100%
            margin 0 auto

            .icon-error {
                width 80px
                height 100%
                margin 0 auto

                i {
                    font-size 80px
                    color #F56C6C

                    height 100%
                    margin 0 auto
                }

                .infoText {
                    font-size 18px
                    color #F56C6C
                    text-align center

                    height 100%
                    margin 0 auto
                }
            }

            .returnText {
                padding-top 10px
                font-size 12px
                color rgb(105, 105, 105)
                text-align center

                height 100%
                margin 0 auto
            }
        }
    }
</style>
