<template>
    <div class="notfound-wrap">
        <Background img-name="background.jpg"
                    :gray="true"></Background>
        <div class="notfound">
            <p class="text-404">404 NotFound</p>
            <p class="text-lose">哎呀，这个页面走丢了~</p>
            <p class="text-timer">{{ timerText }}</p>
        </div>
    </div>
</template>

<script>
    import Background from '../components/Background'

    export default {
        name: "NotFound",
        components: {
            Background
        },
        data() {
            return {
                returnToHome: false,
                autoTime: 5,
                timerText: '5秒后自动返回主页'
            }
        },
        mounted() {
            this.NotFoundTimer();
        },
        methods: {
            NotFoundTimer() {
                var timer = setInterval(() => {
                    this.autoTime--;
                    this.timerText = this.autoTime + '秒后自动返回主页';
                    if (this.autoTime < 0) {
                        this.returnToHome = true;
                        clearInterval(timer);
                    }
                }, 1000)
            }
        },
        watch: {
            returnToHome: function (newVal) {
                if (newVal === true) {
                    this.$router.push({name: 'home'})
                }
            }
        }
    }
</script>

<style lang="stylus">
    .notfound-wrap {
        width 100%
        height 100%

        .notfound {
            position absolute
            top 50%
            left 50%
            transform translate(-50%, -50%)
            width 1200px
            height 400px

            .text-404 {
                font-size 80px
                font-weight bold
                color rgb(63, 63, 63)

                position absolute
                top 30%
                left 50%
                transform translate(-50%, -50%)
            }

            .text-lose {
                font-size 30px
                font-weight bold
                color rgb(105, 105, 105)

                position absolute
                top 50%
                left 50%
                transform translate(-50%, -50%)
            }

            .text-timer {
                font-size 20px
                font-weight bold
                color rgb(105, 105, 105)

                position absolute
                top 75%
                left 50%
                transform translate(-50%, -50%)
            }
        }
    }
</style>
