<template>
    <div class="group-list-wrap">

        <div class="group-list-menu">
            <div class="group-list-menu-left">
                <el-select
                        class="order"
                        v-model="selectedOptions"
                        placeholder="排序方式">
                    <el-option
                            v-for="item in options"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                    </el-option>
                </el-select>

                <el-input class="search" placeholder="搜索...">
                    <el-button slot="append"
                               icon="el-icon-search">
                    </el-button>
                </el-input>
            </div>

            <div class="group-list-menu-right">
                <el-button
                        class="add-btn"
                        icon="el-icon-plus"
                        type="primary">
                    新建用户组
                </el-button>
            </div>
        </div>


    </div>
</template>

<script>
    export default {
        name: "GroupList",
        data() {
            return {
                options: [
                    {
                        value: 'byStartDateTime',
                        label: '按创建时间'
                    },
                    {
                        value: 'byEndDateTime',
                        label: '按结束时间'
                    }
                ],
                selectedOptions: ['byStartDateTime'],
            }
        }
    }
</script>

<style lang="stylus">
    .group-list-wrap {
        width 100%
        height 100%

        .group-list-menu {
            width 100%
            height 40px

            .group-list-menu-left {
                float left
                left 0

                .order {
                    width 120px
                }

                .search {
                    width 200px
                    margin-left 20px
                }
            }

            .group-list-menu-right {
                float right
                right 0
            }
        }
    }
</style>
