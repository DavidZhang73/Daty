<template>
    <div class="user-password-wrap">
        <el-form class="user-password-form"
                 :model="passwords"
                 :rules="rules"
                 ref="passwords"
                 v-if="showForm"
                 label-position="left"
                 label-width="100px">
            <el-form-item prop="firstPassword" label="新密码">
                <el-input
                        type="text"
                        v-model.trim="passwords.firstPassword"
                        placeholder="密码不能为纯数字且须大于8位">
                </el-input>
            </el-form-item>
            <el-form-item prop="secondPassword" label="确认新密码">
                <el-input
                        type="password"
                        v-model.trim="passwords.secondPassword"
                        placeholder="密码不能为纯数字且须大于8位"
                        @keypress.enter.native="submitForm('passwords')">
                </el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="submitForm('passwords')">提交</el-button>
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
        name: "UserPassword",
        data() {
            var validatePassword = (rule, value, callback) => {
                let passwordRex = /^\d+$/;
                if (!value) {
                    return callback(new Error('请输入密码'))
                } else if (value.length > 32 || value.length < 8) {
                    return callback(new Error('密码应该大于8位小于32位'))
                } else if (passwordRex.test(value)) {
                    return callback(new Error('密码不能全是数字'))
                }
                return callback()
            };
            var validateConfirmPassword = (rule, value, callback) => {
                if (!value) {
                    return callback(new Error('请输入确认密码'))
                } else if (value !== this.passwords.firstPassword) {
                    return callback(new Error('两次输入密码不一致'))
                }
                return callback()
            };
            return {
                showForm: true,
                showFeedbackSuccess: false,
                showFeedbackError: false,
                autoTime: 5,
                timerTextSuccess: '5秒后跳转至登陆页面',
                timerTextError: '5秒后返回',
                passwords: {
                    firstPassword: '',
                    secondPassword: '',
                },
                rules: {
                    firstPassword: [
                        {validator: validatePassword, trigger: 'blur'}
                    ],
                    secondPassword: [
                        {validator: validateConfirmPassword, trigger: 'blur'}
                    ]
                }
            };
        },
        methods: {
            submitForm(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        api.resetUserPassword(
                            this.passwords.secondPassword,
                        ).then(data => {
                            if (data.error) {
                                this.changeError();
                            } else {
                                this.changeSuccess();
                            }
                        })
                    }
                });
            },
            logout() {
                api.logout().then(data => {
                    if (data.error) {
                        alert(data.error)
                    } else {
                        this.$store.dispatch('userLogout');
                        this.$router.push({name: 'login'})
                    }
                })
            },
            changeSuccess() {
                this.showForm = false;
                this.showFeedbackSuccess = true;
                this.showFeedbackError = false;
                this.autoTime = 5;
                this.userPasswordTimerSuccess();
            },
            changeError() {
                this.showForm = false;
                this.showFeedbackSuccess = false;
                this.showFeedbackError = true;
                this.autoTime = 5;
                this.userPasswordTimerError();
            },
            userPasswordTimerSuccess() {
                let timer = setInterval(() => {
                    this.autoTime--;
                    this.timerTextSuccess = this.autoTime + '秒后跳转至登陆页面';
                    if (this.autoTime <= 0) {
                        this.logout();
                        clearInterval(timer);
                    }
                }, 1000)
            },
            userPasswordTimerError() {
                let timer = setInterval(() => {
                    this.autoTime--;
                    this.timerTextError = this.autoTime + '秒后返回';
                    if (this.autoTime <= 0) {
                        this.showForm = true;
                        this.showFeedbackSuccess = false;
                        this.showFeedbackError = false;
                        clearInterval(timer);
                    }
                }, 1000)
            },
        },
    }
</script>

<style lang="stylus">
    .user-password-wrap {
        margin-top 50px
        height 100%
        width 100%

        .user-password-form {
            width 60%
            height 100%
            margin-left 60px

            .el-form-item {

                .el-input-group__prepend {
                    text-align center
                    width 70px
                }

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
