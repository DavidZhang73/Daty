<template>
    <div class="aside-wrap">
        <el-col class="aside">
            <el-menu
                    router
                    default-active="1"
                    class="aside-menu"
                    mode="vertical">
                <el-menu-item index="/">home</el-menu-item>
                <el-menu-item index="/about">about</el-menu-item>
            </el-menu>
        </el-col>
    </div>
</template>

<script>
    export default {
        name: "Aside"
    }
</script>

<style lang="stylus">
    .aside-wrap {
        position fixed
        left 0
        top 60px
        height 100%
        width 150px

        .aside {
            height 100%

            .aside-menu {
                height 100%
                background-color rgba(255,255,255,0.8)
            }
        }
    }
</style>