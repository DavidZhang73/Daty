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
            <el-button class="btn-header" type="info" plain v-if="!isAuthorized">注册</el-button>
            <el-button class="btn-header" type="info" plain v-if="!isAuthorized">登录</el-button>
            <el-button class="btn-header" type="info" plain v-if="isAuthorized">登出</el-button>
            <el-button class="btn-header" type="info" plain v-if="isAuthorized">user</el-button>
            <el-menu-item index="/">主页</el-menu-item>
            <el-menu-item index="/about">关于</el-menu-item>
        </el-menu>
    </div>
</template>

<script>
    export default {
        name: "Header",
        data() {
            return {
                isAuthorized: false,
            };
        }
    }
</script>

<style lang="stylus">
    .header-wrap {
        margin-bottom 60px

        .header {
            width 100%
            position fixed
            top 0

            #logo {
                float left
                padding 10px
            }

            .btn-header {
                float right
                margin 10px 3px 10px 3px
            }

            .el-menu-item {
                font-size 20px
            }
        }
    }
</style>