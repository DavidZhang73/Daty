<template>
	<div class="signin-wrap">
		<h1>注册</h1>
		<el-form class="signin-form"
		         status-icon
		         :model="signinForm"
		         :rules="rules"
		         ref="signinForm">
			<el-form-item prop="email">
				<el-tooltip class="item" effect="light" content="Email是您登陆的凭据" placement="top">
					<el-input type="email"
					          v-model.trim="signinForm.email"
					          placeholder="example@abc.com"
					          auto-complete="email">
						<template slot="prepend"><span>*</span>Email</template>
					</el-input>
				</el-tooltip>
			</el-form-item>
			<el-form-item prop="username">
				<el-tooltip class="item" effect="light" content="姓名将有助于别人找到你" placement="top">
					<el-input type="text"
					          v-model.trim="signinForm.username"
					          placeholder="张某某"
					          auto-complete="name">
						<template slot="prepend"><span>*</span>姓名</template>
					</el-input>
				</el-tooltip>
			</el-form-item>
			<el-form-item prop="phone">
				<el-tooltip class="item" effect="light" content="手机号将有助于别人找到你" placement="top">
					<el-input type="text"
					          v-model.trim="signinForm.phone"
					          placeholder="13088888888"
					          auto-complete="tel">
						<template slot="prepend">手机号</template>
					</el-input>
				</el-tooltip>
			</el-form-item>
			<el-form-item prop="qq">
				<el-tooltip class="item" effect="light" content="QQ将有助于别人找到你" placement="top">
					<el-input type="text"
					          v-model.trim="signinForm.qq"
					          placeholder="12348888"
					          auto-complete="qq">
						<template slot="prepend">QQ</template>
					</el-input>
				</el-tooltip>
			</el-form-item>
			<el-form-item prop="password">
				<el-tooltip class="item" effect="light" content="密码" placement="top">
					<el-input type="text"
					          v-model.trim="signinForm.password"
					          placeholder="********"
					          auto-complete="new-password">
						<template slot="prepend"><span>*</span>密码</template>
					</el-input>
				</el-tooltip>
			</el-form-item>
			<el-form-item prop="confirmPassword">
				<el-input type="password"
				          v-model.trim="signinForm.confirmPassword"
				          @keypress.enter.native="submitForm('signinForm')"
				          placeholder="********"
				          auto-complete="new-password">
					<template slot="prepend"><span>*</span>确认密码</template>
				</el-input>
			</el-form-item>
			<div class="info">
				<router-link id="have-account" :to="{name: 'login'}">已经有账号?</router-link>
				<router-link id="forget-password" :to="{name: 'forgetPassword'}">已经有账号只是忘记密码?</router-link>
			</div>
			<el-form-item>
				<el-button type="success" @click="submitForm('signinForm')">注册</el-button>
			</el-form-item>
		</el-form>
	</div>
</template>

<script>
    import api from '../../api'

    export default {
        name: "Signin",
        data() {
            var validateEmail = (rule, value, callback) => {
                let emailRex = /^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$/;
                if (!value) {
                    return callback(new Error('请输入Email'))
                } else if (!emailRex.test(value)) {
                    return callback(new Error('Email格式不正确'))
                } else {
                    return api.checkEmail(value).then(data => {
                        if (data.error) {
                            alert(data.error)
                        } else {
                            if (data.data === 'Email已注册') {
                                return callback(new Error(data.data))
                            } else {
                                return callback()
                            }
                        }
                    });
                }
            };
            var validateUsername = (rule, value, callback) => {
                //必填。150个字符或者更少。包含字母，数字和仅有的@/./+/-/_符号。
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
            var validatePassword = (rule, value, callback) => {
                let passwordRex = /^\d+$/;
                if (!value) {
                    return callback(new Error('请输入密码'))
                } else if (value.length > 32 || value.length < 8) {
                    return callback(new Error('密码应该大于8位小于32位'))
                } else if (value === this.signinForm.name) {
                    return callback(new Error('密码不能和姓名相同'))
                } else if (passwordRex.test(value)) {
                    return callback(new Error('密码不能全是数字'))
                }
                return callback()
            };
            var validateConfirmPassword = (rule, value, callback) => {
                if (!value) {
                    return callback(new Error('请输入确认密码'))
                } else if (value !== this.signinForm.password) {
                    return callback(new Error('确认密码与密码不同'))
                }
                return callback()
            };
            return {
                countdown: 5,
                signinForm: {
                    email: '',
                    username: '',
                    phone: '',
                    qq: '',
                    password: '',
                    confirmPassword: ''
                },
                rules: {
                    email: [
                        {validator: validateEmail, trigger: 'blur'}
                    ],
                    username: [
                        {validator: validateUsername, trigger: 'blur'}
                    ],
                    phone: [
                        {validator: validatePhone, trigger: 'blur'}
                    ],
                    qq: [
                        {validator: validateQQ, trigger: 'blur'}
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
                        api.signin(
                            this.signinForm.email,
                            this.signinForm.username,
                            this.signinForm.phone,
                            this.signinForm.qq,
                            this.signinForm.password,
                        ).then(data => {
                            if (data.error) {
                                this.signinForm.password = '';
                                this.signinForm.confirmPassword = '';
                                this.$message.error({showClose: true, message: data.error})
                            } else {
                                this.$router.push({name: 'emailCheck'})
                            }
                        })
                    } else {
                        return false;
                    }
                });
            },
        }
    }
</script>

<style lang="stylus">
	@import "../../assets/css/consts.styl"
	.signin-wrap {

		h1 {
			margin-bottom 20px
		}

		.signin-form {
			a {
				font-size 12px
				opacity 0.7

				&:hover {
					opacity 1
				}
			}

			label {
				text-align center
			}

			.el-form-item {
				margin-bottom 20px

				input > span {
					color $danger-color
				}

				.el-input-group__prepend {
					text-align center
					width 60px
				}

				.el-button {
					float right
					right 0
				}
			}

			.info {
				margin-bottom 20px

				#have-account {
				}

				#forget-password {
					float right
					right 0
					opacity 0.7

					&:hover {
						opacity 1
					}
				}
			}
		}
	}
</style>
