<template>
    <div class="user-background-wrap">

    </div>
</template>

<script>
    export default {
        name: "UserBackground"
    }
</script>

<style lang="stylus">
    .user-background-wrap {
        background url(../assets/background_img.jpg)
        position absolute
        width 100%
        height 100%
        background-size cover

        &::after {
            content ""
            width 100%
            height 100%
            position absolute
            left 0
            top 0
            background inherit
            filter blur(3px)
            z-index 0
        }
    }
</style>
