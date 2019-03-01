<template>
	<div class="signin-wrap">
		<div class="sign">
			<h1>注册</h1>
			<el-form class="signin-form"
			         :model="signinForm"
			         :rules="rules"
			         ref="signinForm">
				<el-form-item prop="email">
					<el-tooltip class="item" effect="light" content="Email是您登陆的凭据" placement="top">
						<el-input type="email" v-model.trim="signinForm.email" placeholder="example@abc.com">
							<template slot="prepend">Email:</template>
						</el-input>
					</el-tooltip>
				</el-form-item>
				<el-form-item prop="pin">
					<el-tooltip class="item" effect="light" content="请您将邮箱中的验证码复制到这里" placement="top">
						<el-input type="text" v-model.trim="signinForm.pin" placeholder="1234">
							<template slot="prepend">验证码</template>
							<el-button slot="append" icon="el-icon-message"> 发送验证码</el-button>
						</el-input>
					</el-tooltip>
				</el-form-item>
				<el-form-item prop="name">
					<el-tooltip class="item" effect="light" content="姓名将有助于别人找到你" placement="top">
						<el-input type="text" v-model.trim="signinForm.name" placeholder="某某某">
							<template slot="prepend">姓名</template>
						</el-input>
					</el-tooltip>
				</el-form-item>
				<el-form-item prop="phone">
					<el-tooltip class="item" effect="light" content="手机号将有助于别人找到你" placement="top">
						<el-input type="text" v-model.trim="signinForm.phone" placeholder="13088888888">
							<template slot="prepend">手机号</template>
						</el-input>
					</el-tooltip>
				</el-form-item>
				<el-form-item prop="password">
					<el-tooltip class="item" effect="light" content="密码包含" placement="top">
						<el-input type="text" v-model.trim="signinForm.password" placeholder="********">
							<template slot="prepend">密码</template>
						</el-input>
					</el-tooltip>
				</el-form-item>
				<el-form-item prop="confirmPassword">
					<el-input type="password" v-model.trim="signinForm.confirmPassword" placeholder="********">
						<template slot="prepend">确认密码</template>
					</el-input>
				</el-form-item>
				<div class="info">
					<router-link id="have-account" :to="{name: 'login'}">已经有账号?</router-link>
					<router-link id="forget-password" :to="{name: 'forget-password-step1'}">已经有账号只是忘记密码?</router-link>
				</div>
				<el-form-item>
					<el-button type="success" @click="submitForm('signinForm')">注册</el-button>
				</el-form-item>
			</el-form>
		</div>
	</div>
</template>

<script>
    export default {
        name: "Signin",
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
            var validateName = (rule, value, callback) => {
                if (!value) {
                    return callback(new Error('请输入姓名'))
                }
                return callback()
            };
            var validatePhone = (rule, value, callback) => {
                let phoneRex = /^1[34578]\d{9}$/;
                if (!value) {
                    return callback(new Error('请输入手机号'))
                }
                if (!phoneRex.test(value)) {
                    return callback(new Error('手机号格式不正确'))
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
                if (value === this.signinForm.name) {
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
                if (value !== this.signinForm.confirmPassword) {
                    return callback(new Error('确认密码与密码不同'))
                }
                return callback()
            };
            return {
                signinForm: {
                    email: '',
                    pin: '',
                    name: '',
                    phone: '',
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
                    name: [
                        {validator: validateName, trigger: 'blur'}
                    ],
                    phone: [
                        {validator: validatePhone, trigger: 'blur'}
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
            ,
            getBGImageURL() {
                // TODO
                let url = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN';
                return 'url(' + url + ')';
            }
        }
    }
</script>

<style lang="stylus">
	.signin-wrap {
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

		.sign {
			position fixed
			top 50%
			right 50%
			width 500px
			margin -280px -290px 0 0
			padding 40px 40px
			border-radius 5px
			box-shadow 0 0 5px #2c3e50
			background-color: #fbfbfb
			z-index 1

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
						padding-left 5px
					}

					#forget-password {
						float right
						right 0
						padding-right 5px
						opacity 0.7

						&:hover {
							opacity 1
						}
					}
				}
			}
		}
	}
</style>
