<template>
    <div class="about-wrap">
        <el-row class="about-row" :gutter="20">
            <el-col
                    v-for="(dev, index) in dev_list"
                    :key="dev.id"
                    :span="2"
                    :offset="index > 0 ? 2 : 3">
                <el-card
                        :body-style="{ padding: '0px' }"
                        class="row-card"
                        shadow="always">
                    <img :src="dev.imgURL" class="image">
                    <div class="card-text">
                        <el-row>
                            <span style="font-size: 18px;">{{dev.name}}</span>
                        </el-row>
                        <el-row>
                            <el-button type="text" style="font-size: 13px;">
                                <a :href="dev.pageURL" target="_blank">Github</a>
                            </el-button>
                        </el-row>
                    </div>
                </el-card>
            </el-col>
        </el-row>
    </div>
</template>

<script>

    export default {
        name: 'about',
        components: {},
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
                        name: 'EggTargaryen',
                        imgURL: 'https://avatars1.githubusercontent.com/u/34475415?s=460&v=4',
                        pageURL: 'https://github.com/dzxrly',
                        desc: 'desc4'
                    }
                ]
            }
        }
    }

</script>

<style lang="stylus">
    .about-wrap {
        height 100%
        background-color #F8F9FB

        .about-row {
            padding-top 260px

            .row-card {
                width 150px

                .image {
                    width 150px
                    height 150px
                    margin-bottom 5px
                }

                .card-text {
                    width 150px

                    span {
                        margin 10px 10px 0 10px
                    }

                    .el-button {
                        float right
                        padding 5px

                        a {
                            color #409eff
                        }
                    }
                }
            }
        }
    }
</style>
