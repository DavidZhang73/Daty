<template>
    <div class="footer-wrap">
        <p>Copyright© {{year()}} <a href="https://github.com/DavidZhang73/daty.git" target="_blank">Github</a></p>
    </div>
</template>

<script>
    export default {
        name: "Footer",
        methods: {
            year: function () {
                return (new Date()).getFullYear();
            }
        }
    }
</script>

<style lang="stylus">
    .footer-wrap {
        width 100%
        height 30px
        position fixed
        bottom 0
        background-color #ffffff
        box-shadow 0 -2px 6px 0 rgba(0,0,0,0.12)

        p {
            margin 5px
            text-align center
            opacity 1

            a:hover {
                opacity 0.6
            }
        }
    }
</style>