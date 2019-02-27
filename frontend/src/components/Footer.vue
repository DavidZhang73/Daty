<template>
    <div class="footer-wrap">
        <div class="footer">
            <p>Copyright© {{year()}} <a href="https://github.com/DavidZhang73/daty.git" target="_blank">Github</a></p>
        </div>
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
        .footer {
            height 30px
            width 100%
            position fixed
            bottom 0
            background-color #DCDCDC

            p {
                text-align center
                margin 7px 10px
                font-size 1em
            }
        }
    }
</style>