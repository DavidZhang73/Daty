<template>
    <div class="header-wrap">
        <el-menu
                :default-active="activeIndex"
                class="el-menu-demo"
                mode="horizontal"
                background-color="#DCDCDC"
                text-color="#000"
                active-text-color="#000000">
            <img id="logo" src="../assets/logo.png" height="40px" width="40px">
            <el-button id="logoin" type="info" plain>登录</el-button>
            <el-button id="register" type="info" plain>注册</el-button>
            <el-menu-item index="1">
                <router-link :to="{name : 'home'}">主页</router-link>
            </el-menu-item>
            <el-menu-item index="2">
                <router-link :to="{name : 'about'}">关于</router-link>
            </el-menu-item>
        </el-menu>

    </div>
</template>

<script>
    export default {
        name: "Header",
        data() {
            return {
                activeIndex: '1'
            };
        }
    }
</script>

<style lang="stylus">
    #logo {
        float left
        padding 10px
    }

    #logoin {
        float right
        margin 10px
    }

    #register {
        float right
        margin 10px
    }
</style>