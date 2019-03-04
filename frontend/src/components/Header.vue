<template>
	<div class="header-wrap">
		<el-menu
			router
			:default-active="$route.path"
			class="header"
			mode="horizontal"
			background-color="#DCDCDC"
			text-color="#000"
			active-text-color="#000000">
			<img id="logo" src="../assets/logo.png" height="40px" width="80px">
			<el-button-group class="btn-header" v-if="!isLogin()">
				<router-link class="el-button el-button--info is-plain" :to="{name: 'login'}">登录</router-link>
				<router-link class="el-button el-button--info is-plain" :to="{name: 'signin'}">注册</router-link>
			</el-button-group>
			<el-button-group class="btn-header" v-if="isLogin()">
				<router-link class="el-button el-button--info is-plain"
				             :to="{name: 'home'}"
				             v-cloak>
					{{$store.state.user.username}}
				</router-link>
				<button class="el-button el-button--info is-plain" @click="logout">登出</button>
			</el-button-group>
			<el-menu-item index="/">主页</el-menu-item>
			<el-menu-item index="/about">关于</el-menu-item>
		</el-menu>
	</div>
</template>

<script>
    import api from '../api'

    export default {
        name: "Header",
        data() {
            return {}
        },
        methods: {
            logout() {
                api.logout().then(data => {
                    if (data.error) {
                        alert(data.error)
                    } else {
                        this.$store.commit('userMutation', null);
                        this.$router.push({name: 'home'})
                    }
                })
            },
            isLogin() {
                return this.$store.state.user
            }
        }
    }
</script>

<style lang="stylus">
	.header-wrap {
		.header {
			width 100%
			position fixed
			top 0
			z-index 1

			#logo {
				float left
				padding 10px
			}

			.btn-header {
				float right
				margin 10px 10px 10px 0
			}

			.el-menu-item {
				font-size 20px
			}
		}
	}
</style>
