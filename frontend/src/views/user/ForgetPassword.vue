<template>
	<div class="forget-password-wrap">
		<h1>找回密码</h1>
		<el-form class="forgrt-password-form"
		         :model="forgetPasswordForm"
		         :rules="rules"
		         ref="forgetPasswordForm">
			<el-form-item prop="email">
				<el-tooltip class="item" effect="light" content="您要找回的Email" placement="top">
					<el-input type="email"
					          v-model.trim="forgetPasswordForm.email"
					          @keypress.enter.native="submitForm('forgetPasswordForm')"
					          placeholder="example@abc.com"
					          auto-complete="email">
						<template slot="prepend">Email:</template>
					</el-input>
				</el-tooltip>
			</el-form-item>
			<el-form-item>
				<el-button type="primary" @click="submitForm('forgetPasswordForm')">找回密码</el-button>
			</el-form-item>
		</el-form>
	</div>
</template>

<script>
    import api from '../../api'

    export default {
        name: "ForgetPassword",
        data() {
            var validateEmail = (rule, value, callback) => {
                let emailRex = /^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$/;
                if (!value) {
                    return callback(new Error('请输入Email'))
                } else if (!emailRex.test(value)) {
                    return callback(new Error('Email格式不正确'))
                } else {
                    return api.forgetPasswordEmailCheck(value).then(data => {
                        if (data.error) {
                            this.$message.error({showClose: true, mseeage: data.error});
                        } else {
                            if (data.data === 'Email不存在') {
                                return callback(new Error(data.data))
                            } else {
                                return callback()
                            }
                        }
                    });
                }
            };
            return {
                forgetPasswordForm: {
                    email: '',
                },
                rules: {
                    email: [
                        {validator: validateEmail, trigger: 'blur'}
                    ]
                },
                countdown: 5,
            };
        },
        methods: {
            submitForm(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        api.forgetPassword(this.forgetPasswordForm.email).then(data => {
                            if (data.error) {
                                this.$message.error({showClose: true, message: data.error})
                            } else {
                                this.$message.success({
                                    duration: this.countdown * 1000,
                                    message: `找回成功！请在邮箱中继续操作，${this.countdown}秒后跳转到主页`
                                });
                                let timer = setInterval(() => {
                                    if (this.countdown === 0) {
                                        clearInterval(timer);
                                        this.$router.push({name: 'home'})
                                    }
                                    this.countdown--
                                }, 1000);
                            }
                        })
                    } else {
                        return false;
                    }
                });
            }
        }
    }
</script>

<style lang="stylus">
	.forget-password-wrap {

		h1 {
			margin-bottom 20px
		}

		.forgrt-password-form {
			label {
				text-align center
			}

			.el-form-item {
				margin-bottom 20px

				.el-input-group__prepend {
					text-align center
					width 60px
				}

				.el-button {
					float right
					right 0
				}
			}
		}
	}
</style>
