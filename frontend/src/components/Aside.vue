<template>
    <div class="aside-wrap">
        <el-col class="aside" :span="4">
            <el-menu
                    router
                    default-active="1"
                    class="el-menu-vertical-demo"
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
        position relative
        height 100%
        left 0

    }
</style>