<template>
    <div class="about-wrap">
        <Background img-name="background.jpg"
                    :blur="true"></Background>
        <div class="about">
            <h1>Developers</h1>
            <div class="card"
                 v-for="dev in dev_list"
                 :key="dev.id">
                <a :href="dev.pageURL" target="_blank">
                    <img class="dev-image" :src="dev.imgURL" :alt="dev.name">
                    <span class="dev-name">{{dev.name}}</span>
                    <span class="dev-link">Github</span>
                </a>
            </div>
        </div>
    </div>
</template>

<script>
    import Background from '../components/Background'

    export default {
        name: 'about',
        components: {
            Background
        },
        data() {
            return {
                dev_list: [
                    {
                        id: 0,
                        name: 'DavidBill',
                        imgURL: 'https://avatars2.githubusercontent.com/u/33928385?s=460&v=4',
                        pageURL: 'https://github.com/DavidZhang73',
                        desc: 'desc0'
                    },
                    {
                        id: 1,
                        name: 'EggTargaryen',
                        imgURL: 'https://avatars1.githubusercontent.com/u/34475415?s=460&v=4',
                        pageURL: 'https://github.com/dzxrly',
                        desc: 'desc1'
                    },
                    {
                        id: 2,
                        name: 'Abraham cb',
                        imgURL: 'https://avatars1.githubusercontent.com/u/32613101?s=400&v=4',
                        pageURL: 'https://github.com/Miraclecb',
                        desc: 'desc2'
                    },
                    {
                        id: 3,
                        name: 'xiaotxiaox',
                        imgURL: 'https://avatars2.githubusercontent.com/u/38485069?s=400&v=4',
                        pageURL: 'https://github.com/xiaotxiaox',
                        desc: 'desc3'
                    },
                    {
                        id: 4,
                        name: 'Victor',
                        imgURL: 'https://avatars1.githubusercontent.com/u/38451914?s=400&v=4',
                        pageURL: 'https://github.com/VictorYgy',
                        desc: 'desc4'
                    }
                ]
            }
        }
    }

</script>

<style lang="stylus">
    .about-wrap {
        .about {
            position relative
            padding-top 150px

            h1 {
                font-size 2em
                text-align center
                padding-bottom 40px
            }

            .card {
                float left
                width 200px
                margin 0 50px 50px 50px
                border-radius 20px
                background-color rgb(249, 250, 254)
                box-shadow 0 0 6px 0 rgba(0, 0, 0, 0.12)
                overflow hidden

                &:hover {
                    box-shadow 0 0 10px 0 #7fbcff
                }

                .dev-image {
                    width 200px
                    height 200x
                    margin-bottom 5px
                }

                .dev-name {
                    font-size 1.8em
                    display block
                    padding 5px 0 0 5px
                    margin-bottom 10px
                }

                .dev-link {
                    float right
                    padding 5px
                }
            }
        }
    }
</style>
