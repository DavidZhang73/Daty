<template>
	<div class="login-wrap">
		<UserBackground></UserBackground>
		<div class="login">
			<router-link :to="{name: 'home'}">
				<img class="logo" src="../assets/logo.png">
			</router-link>
			<el-form class="login-form"
			         :model="loginForm"
			         :rules="rules"
			         ref="loginForm">
				<el-form-item prop="email">
					<el-input type="email" v-model.trim="loginForm.email">
						<template slot="prepend">Email:</template>
					</el-input>
				</el-form-item>
				<el-form-item prop="password">
					<el-input type="password"
					          v-model.trim="loginForm.password"
					          @keypress.enter.native="submitForm('loginForm')">
						<template slot="prepend">密码</template>
					</el-input>
				</el-form-item>
				<div class="info">
					<router-link id="no-account" :to="{name: 'signin'}">还没有账号?</router-link>
					<router-link id="forget-password" :to="{name: 'forgetPassword'}">忘记密码?</router-link>
				</div>
				<el-form-item>
					<el-button type="primary" @click="submitForm('loginForm')">登陆</el-button>
				</el-form-item>
			</el-form>
		</div>
	</div>
</template>

<script>
    import api from '../api'
    import UserBackground from '../components/UserBackground'

    export default {
        name: "Login",
        components: {
            UserBackground
        },
        data() {
            var validateEmail = (rule, value, callback) => {
                let emailRex = /^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$/;
                if (!value) {
                    return callback(new Error('请输入Email'))
                } else if (!emailRex.test(value)) {
                    return callback(new Error('Email格式不正确'))
                }
                return callback()
            };
            var validatePassword = (rule, value, callback) => {
                if (!value) {
                    return callback(new Error('请输入密码'))
                } else if (value.length > 32) {
                    return callback(new Error('密码过长, 应该小于32位'))
                }
                return callback()
            };
            return {
                loginForm: {
                    email: '',
                    password: '',
                },
                rules: {
                    email: [
                        {validator: validateEmail, trigger: 'blur'}
                    ],
                    password: [
                        {validator: validatePassword, trigger: 'blur'}
                    ]
                }
            };
        },
        methods: {
            submitForm(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        api.login(this.loginForm.email, this.loginForm.password).then(data => {
                            if (data.error) {
                                this.loginForm.password = '';
                                this.$message.error({showClose: true, message: data.error})
                            } else {
                                this.$store.commit('userMutation', {
                                    email: data.data.email,
                                    username: data.data.username,
                                    phone: data.data.phone,
                                    qq: data.data.qq
                                });
                                this.$router.push({name: 'home'})
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
	@import "../assets/css/consts.styl"
	.login-wrap {

		.login {
			position absolute
			top 50%
			right 50%
			width 400px
			margin -230px -240px 0 0
			padding 40px 40px
			border-radius 5px
			box-shadow 0 0 10px #2c3e50
			background-color: #fbfbfb
			z-index 1

			.logo {
				height 80px
				width 160px
				padding 10px 5px
				margin 10px 0 30px 0
			}

			.login-form {
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
					margin 0 0 30px 0

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
					margin-bottom 15px

					#no-account {
					}

					#forget-password {
						float right
						right 0
					}
				}
			}
		}
	}
</style>
