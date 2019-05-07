<template>
    <div class="aside-wrap">
        <div class="aside-lg hidden-sm-and-down" :style="asideWidth">
            <el-menu
                    router
                    :default-active="$route.path"
                    class="aside-menu">
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

        <div class="aside-sm hidden-lg-and-up" :style="asideWidth">
            <el-menu
                    router
                    :default-active="$route.path"
                    class="aside-menu">
                <el-submenu index="1">
                    <template slot="title">
                        <i class="el-icon-menu"></i>
                    </template>
                </el-submenu>
                <el-submenu index="2">
                    <template slot="title">
                        <i class="el-icon-setting"></i>
                    </template>
                </el-submenu>
            </el-menu>
        </div>
    </div>
</template>

<script>
    import 'element-ui/lib/theme-chalk/display.css'

    export default {
        name: "Aside",
        data() {
            return {
                asideWidth: '',
                screenWidth: document.body.clientWidth,
            }
        },
        mounted() {
            var _this = this;
            window.onresize = function () {
                _this.screenWidth = document.documentElement.clientWidth;
            };
            if (_this.screenWidth >= 1200) {
                _this.asideWidth = 'width: 200px;';
            } else if (_this.screenWidth >= 768 && _this.screenWidth < 1200) {
                _this.asideWidth = 'width: 50px;'
            }
        },
        watch: {
            'screenWidth': function (newVal) {
                if (newVal >= 1200) {
                    this.asideWidth = 'width: 200px;';
                } else if (newVal >= 768 && newVal < 1200) {
                    this.asideWidth = 'width: 50px;'
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

        .aside-lg {
            height 100%

            .aside-menu {
                height 100%

            }
        }
    }
</style>
