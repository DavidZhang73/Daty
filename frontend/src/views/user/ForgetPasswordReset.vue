<template>
	<div class="forget-password-reset-wrap">
		<h1>重置密码</h1>
		<el-form class="forgrt-password-reset-form"
		         :model="forgetPasswordResetForm"
		         :rules="rules"
		         ref="forgetPasswordResetForm">
			<el-form-item prop="password">
				<el-tooltip class="item" effect="light" content="密码" placement="top">
					<el-input type="text"
					          v-model.trim="forgetPasswordResetForm.password"
					          placeholder="********"
					          auto-complete="new-password">
						<template slot="prepend">新密码</template>
					</el-input>
				</el-tooltip>
			</el-form-item>
			<el-form-item prop="confirmPassword">
				<el-input type="password"
				          v-model.trim="forgetPasswordResetForm.confirmPassword"
				          @keypress.enter.native="submitForm('forgetPasswordResetForm')"
				          placeholder="********"
				          auto-complete="new-password">
					<template slot="prepend">确认密码</template>
				</el-input>
			</el-form-item>
			<el-form-item>
				<el-button type="success" @click="submitForm('forgetPasswordResetForm')">重置密码</el-button>
			</el-form-item>
		</el-form>
	</div>
</template>

<script>
    import api from '../../api'

    export default {
        name: "ForgetPasswordReset",
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
                } else if (value !== this.forgetPasswordResetForm.password) {
                    return callback(new Error('确认密码与密码不同'))
                }
                return callback()
            };
            return {
                forgetPasswordResetForm: {
                    password: '',
                    confirmPassword: ''
                },
                rules: {
                    password: [
                        {validator: validatePassword, trigger: 'blur'}
                    ],
                    confirmPassword: [
                        {validator: validateConfirmPassword, trigger: 'blur'}
                    ]
                },
                countdown: 5,
            };
        },
        methods: {
            submitForm(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        api.forgetPasswordReset(this.$route.params.uuid, this.forgetPasswordResetForm.password).then(data => {
                            if (data.error) {
                                this.$message.error({showClose: true, message: data.error})
                            } else {
                                this.$router.push({name: 'forgetPasswordResetSuccess'})
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
	.forget-password-reset-wrap {

		h1 {
			margin-bottom 20px
		}

		.forgrt-password-reset-form {
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
