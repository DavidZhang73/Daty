<template>
	<div class="login-wrap">
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
					<el-input type="password" v-model.trim="loginForm.password">
						<template slot="prepend">密码</template>
					</el-input>
				</el-form-item>
				<div class="info">
					<router-link id="no-account" :to="{name: 'signin'}">还没有账号?</router-link>
					<router-link id="forget-password" :to="{name: 'forget-password-step1'}">忘记密码?</router-link>
				</div>
				<el-form-item>
					<el-button type="primary" @click="submitForm('loginForm')">登陆</el-button>
				</el-form-item>
			</el-form>
		</div>
	</div>
</template>

<script>
    export default {
        name: "Login",
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
            var validatePassword = (rule, value, callback) => {
                if (!value) {
                    return callback(new Error('请输入密码'))
                }
                if (value.length > 32) {
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
                        console.log(this.loginForm);
                        alert('submit!');
                    } else {
                        console.log('error submit!!');
                        return false;
                    }
                });
            },
            getBGImageURL() {
                // TODO
                let url = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN';
                return url;
            }
        }
    }
</script>

<style lang="stylus">

	.login-wrap {
		background: url(https://cn.bing.com/az/hprichbg/rb/PolarBearDay_ZH-CN5185516722_1920x1080.jpg)
		position absolute
		width 100%
		height 100%
		background-size cover;

		&::after {
			content: "";
			width: 100%;
			height: 100%;
			position: absolute;
			left: 0;
			top: 0;
			background: inherit;
			filter: blur(5px);
			z-index 0
		}

		.login {
			position fixed
			top 50%
			right 50%
			width 400px
			margin -230px -240px 0 0
			padding 40px 40px
			border-radius 5px
			box-shadow 0 0 5px #2c3e50
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
					margin-bottom 20px

					#no-account {
						margin-left 5px

					}

					#forget-password {
						float right
						right 0
						padding-right 10px
					}
				}
			}
		}
	}
</style>
