<template>
    <div class="header-wrap">
        <el-menu
                router
                :default-active="menuIndex"
                class="header"
                mode="horizontal"
                background-color="#FFFFFF"
                text-color="#000"
                active-text-color="#000000">
            <img id="logo" src="../assets/logo_svg.svg" height="40px" width="80px">
            <el-button-group class="btn-header" v-if="!isAuthorized()">
                <router-link
                        class="el-button el-button--info is-plain"
                        :to="{name: 'login'}">
                    登录
                </router-link>
                <router-link
                        class="el-button el-button--info is-plain"
                        :to="{name: 'signin'}">
                    注册
                </router-link>
            </el-button-group>
            <el-button-group class="btn-header" v-if="isAuthorized()">
                <router-link
                        class="el-button el-button--info is-plain"
                        :to="{name: 'home'}">
                    USER
                </router-link>
                <button
                        class="el-button el-button--info is-plain"
                        :to="{name: 'home'}"
                        @click="logout">
                    登出
                </button>
            </el-button-group>
            <el-menu-item index="0" style="margin: 0px; padding: 0px;"></el-menu-item>
            <el-menu-item index="/" @click="goToHome">主页</el-menu-item>
            <el-menu-item index="/about" @click="goToAbout">关于</el-menu-item>
        </el-menu>
    </div>
</template>

<script>

    export default {
        name: "Header",
        data() {
            return {
                menuIndex: '/'
            }
        },
        methods: {
            logout() {
                alert("logout")
            },
            isAuthorized() {
                return false
            },
            goToHome() {
                this.menuIndex = '/'
            },
            goToAbout() {
                this.menuIndex = '/about'
            }
        },
        watch: {
            '$route.path': function (newVal, oldVal) {
                if (newVal !== '/' && newVal !== '/about') {
                    this.menuIndex = '0'
                }
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
            box-shadow 0 2px 6px 0 rgba(0, 0, 0, 0.12)

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
