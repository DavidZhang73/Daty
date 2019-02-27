<template>
    <div class="about-wrap">
        <el-row class="about-row1">
            <el-card :body-style="{ padding: '0px' }" class="row1-card1" shadow="always">
                <img src="../assets/DavidBill-github.png" class="image">
                <div class="card1-text">
                    <el-row>
                        <span style="font-size: 20px;">DavidBill</span>
                    </el-row>
                    <el-row>
                        <el-button type="text" style="font-size: 14px;" align="right">Github</el-button>
                    </el-row>
                </div>
            </el-card>
        </el-row>
    </div>
</template>

<script>

    export default {
        name: 'about',
        components: {}
    }
</script>

<style lang="stylus">
    .about-wrap {
        height 100%
        margin-left 150px

        .about-row1 {

            .row1-card1 {
                width 236px

                .image {
                    width 100%
                    display block
                }

                .card1-text {
                    width 100%
                }
            }
        }
    }
</style>
