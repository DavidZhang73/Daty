<template>
    <el-row class="collection-list-wrap">
        <el-col class="collection-list-menu"
                :xs="{span:24}"
                :sm="{span:20,offset:2}"
                :lg="{span:16,offset:4}">
            <el-select class="order"
                       placeholder="按时间排序"
                       v-model="params.type"
                       @change="getOrUpdateCollectionList()"
                       clearable>
                <el-option
                        v-for="item in options"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                </el-option>
            </el-select>
            <el-input class="search" placeholder="搜索..." v-model="params.search">
                <el-button slot="append"
                           icon="el-icon-search"
                           @click="getOrUpdateCollectionList()">
                    搜索
                </el-button>
            </el-input>
            <el-button
                    class="clearBtn"
                    icon="el-icon-delete"
                    @click="clearSearch();getOrUpdateCollectionList();">清空搜索
            </el-button>
            <router-link :to="{name : 'home'}">
                <el-button
                        class="addBtn"
                        icon="el-icon-plus"
                        type="primary">
                    新建文件集
                </el-button>
            </router-link>
        </el-col>
    </el-row>
</template>

<script>
    export default {
        name: "CollectionList",
        data() {
            return {
                params: {
                    page: 1,
                    search: '',
                    type: '',
                    ordering: '',
                },
                options: [],
            }
        },
        methods: {
            getOrUpdateCollectionList() {
                //TODO
            },
            clearSearch() {
                this.params.search = '';
            },
        }
    }
</script>

<style lang="stylus">
    .collection-list-wrap {

        .collection-list-menu {

            .order {
                width 160px
            }

            .search {
                width 250px
                margin-left 10px
            }

            .clearBtn {
                width 120px
                margin-left 10px
            }

            .addBtn {
                float right
                right 0
                width 140px
            }
        }

    }
</style>
