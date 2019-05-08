<template>
    <div class="aside-wrap" :style="asideWidth">
        <div class="aside" v-if="showAside">
            <el-menu
                    router
                    :default-active="$route.path"
                    class="aside-menu"
                    :collapse="isCollapse">
                <el-submenu index="1">
                    <template slot="title">
                        <i class="el-icon-menu"></i>
                        <span>管理</span>
                    </template>
                    <el-menu-item index="/center/collectionList">文件集</el-menu-item>
                    <el-menu-item index="/center/groupList">用户组</el-menu-item>
                </el-submenu>
                <el-submenu index="2">
                    <template slot="title">
                        <i class="el-icon-setting"></i>
                        <span>用户</span>
                    </template>
                    <el-menu-item index="/center/userInfo">修改信息</el-menu-item>
                    <el-menu-item index="/center/userPassword">修改密码</el-menu-item>
                </el-submenu>
            </el-menu>
        </div>
    </div>
</template>

<script>
    import 'element-ui/lib/theme-chalk/display.css'

    export default {
        name: "Aside",
        props: {
            screenWidth: Number
        },
        data() {
            return {
                isCollapse: false,
                showAside: false,
                asideWidth: '',
            }
        },
        mounted() {
            if (this.screenWidth >= 1200) {
                this.asideWidth = 'width: 200px;';
                this.showAside = true;
                this.isCollapse = false;
            } else if (this.screenWidth >= 768 && this.screenWidth < 1200) {
                this.asideWidth = 'width: 50px;';
                this.showAside = true;
                this.isCollapse = true;
            }
        },
        watch: {
            'screenWidth': function (newVal) {
                if (newVal >= 1200) {
                    this.asideWidth = 'width: 200px;';
                    this.showAside = true;
                    this.isCollapse = false;
                } else if (newVal >= 768 && newVal < 1200) {
                    this.asideWidth = 'width: 50px;';
                    this.showAside = true;
                    this.isCollapse = true;
                }
            }
        },
        methods: {}
    }
</script>

<style lang="stylus">
    .aside-wrap {
        position fixed
        left 0
        top 60px
        bottom 30px
        height 100%

        .aside {
            height 100%

            .aside-menu {
                height 100%

            }
        }
    }
</style>
