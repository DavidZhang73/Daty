<template>
	<div class="forget-password-wrap">
		<UserBackground></UserBackground>
		<div class="forget-password">
			<h1>找回密码</h1>
			<el-form class="forgrt-password-form"
			         :model="forgetPasswordForm"
			         :rules="rules"
			         ref="signinForm">
				<el-form-item prop="email">
					<el-tooltip class="item" effect="light" content="您要找回的Email" placement="top">
						<el-input type="email" v-model.trim="forgetPasswordForm.email" placeholder="example@abc.com">
							<template slot="prepend">Email:</template>
						</el-input>
					</el-tooltip>
				</el-form-item>
				<el-form-item prop="pin">
					<el-tooltip class="item" effect="light" content="请您将邮箱中的验证码复制到这里" placement="top">
						<el-input type="text" v-model.trim="forgetPasswordForm.pin" placeholder="1234">
							<template slot="prepend">验证码</template>
							<el-button slot="append" icon="el-icon-message"> 发送验证码</el-button>
						</el-input>
					</el-tooltip>
				</el-form-item>
				<el-form-item prop="password">
					<el-tooltip class="item" effect="light" content="密码包含" placement="top">
						<el-input type="text" v-model.trim="forgetPasswordForm.password" placeholder="********">
							<template slot="prepend">新密码</template>
						</el-input>
					</el-tooltip>
				</el-form-item>
				<el-form-item prop="confirmPassword">
					<el-input type="password" v-model.trim="forgetPasswordForm.confirmPassword" placeholder="********">
						<template slot="prepend">确认密码</template>
					</el-input>
				</el-form-item>
				<el-form-item>
					<el-button type="success" @click="submitForm('forgetPasswordForm')">提交</el-button>
				</el-form-item>
			</el-form>
		</div>
	</div>
</template>

<script>
    import UserBackground from '../components/UserBackground'

    export default {
        name: "ForgetPassword",
        components: {
            UserBackground
        },
        data() {
            var validateEmail = (rule, value, callback) => {
                let emailRex = /^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$/;
                if (!value) {
                    return callback(new Error('请输入Email'))
                }
                if (!emailRex.test(value)) {
                    return callback(new Error('Email格式不正确'))
                }
                return callback()
            };
            var validatePin = (rule, value, callback) => {
                if (!value) {
                    return callback(new Error('请输入验证码'));
                }
                if (value.length !== 4) {
                    return callback(new Error('验证码应该是4位的'));
                }
                return callback()
            };
            var validatePassword = (rule, value, callback) => {
                let passwordRex = /^\d+$/;
                if (!value) {
                    return callback(new Error('请输入密码'))
                }
                if (value.length > 32 || value.length < 8) {
                    return callback(new Error('密码应该大于8位小于32位'))
                }
                if (value === this.forgetPasswordForm.name) {
                    return callback(new Error('密码不能和姓名相同'))
                }
                if (passwordRex.test(value)) {
                    return callback(new Error('密码不能全是数字'))
                }
                return callback()
            };
            var validateConfirmPassword = (rule, value, callback) => {
                if (!value) {
                    return callback(new Error('请输入确认密码'))
                }
                if (value !== this.forgetPasswordForm.password) {
                    return callback(new Error('确认密码与密码不同'))
                }
                return callback()
            };
            return {
                forgetPasswordForm: {
                    email: '',
                    pin: '',
                    password: '',
                    confirmPassword: ''
                },
                rules: {
                    email: [
                        {validator: validateEmail, trigger: 'blur'}
                    ],
                    pin: [
                        {validator: validatePin, trigger: 'blur'}
                    ],
                    password: [
                        {validator: validatePassword, trigger: 'blur'}
                    ],
                    confirmPassword: [
                        {validator: validateConfirmPassword, trigger: 'blur'}
                    ]
                }
            };
        },
        methods: {
            submitForm(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        alert('submit!');
                        console.log('submit!');
                        return false;
                    } else {
                        console.log('error submit!!');
                        return false;
                    }
                });
            }
        }
    }
</script>

<style lang="stylus">
	.forget-password-wrap {
		.forget-password {
			position fixed
			top 50%
			right 50%
			width 500px
			margin -200px -290px 0 0
			padding 40px 40px
			border-radius 5px
			box-shadow 0 0 10px #2c3e50
			background-color: #fbfbfb
			z-index 1

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
	}
</style>
