<template>
	<div class="group-list-wrap">

		<div class="group-list-menu">
			<div class="group-list-menu-left">
				<el-select
					clearable="true"
					class="order"
					v-model="params.type"
					placeholder="按类别筛选"
					@change="getOrUpdateGroupInfo()">
					<el-option
						v-for="item in options"
						:key="item.value"
						:label="item.label"
						:value="item.value">
					</el-option>
				</el-select>

				<el-input class="search" placeholder="搜索..." v-model="params.search" clearable>
					<el-button slot="append"
					           icon="el-icon-search"
					           @click="getOrUpdateGroupInfo()">
					</el-button>
				</el-input>
			</div>

			<div class="group-list-menu-right">
				<el-button
					class="add-btn"
					icon="el-icon-plus"
					type="primary"
					@click="addNewGroup()">
					新建用户组
				</el-button>
			</div>
		</div>

		<el-table :data="tableData">
			<el-table-column
				label="序号">
				<template slot-scope="scope">
					<span style="margin-left: 10px">{{ scope.row.id }}</span>
				</template>
			</el-table-column>
			<el-table-column
				label="用户组名称">
				<template slot-scope="scope">
					<span style="margin-left: 10px">{{ scope.row.name }}</span>
				</template>
			</el-table-column>
			<el-table-column
				label="用户组人数">
				<template slot-scope="scope">
					<span style="margin-left: 10px">{{ scope.row.users_count }}</span>
				</template>
			</el-table-column>
			<el-table-column
				label="创建日期">
				<template slot-scope="scope">
					<i class="el-icon-time"></i>
					<span style="margin-left: 10px">{{ scope.row.created_datetime }}</span>
				</template>
			</el-table-column>
			<el-table-column
				label="上次修改日期">
				<template slot-scope="scope">
					<i class="el-icon-time"></i>
					<span style="margin-left: 10px">{{ scope.row.last_modified_datetime }}</span>
				</template>
			</el-table-column>
			<el-table-column label="操作">
				<template slot-scope="scope">
					<el-button
						type="info"
						size="mini"
						@click="handleEdit(scope.$index, scope.row)">
						编辑
					</el-button>
				</template>
			</el-table-column>
		</el-table>

		<el-pagination
			@size-change="getOrUpdateGroupInfo()"
			@current-change="getOrUpdateGroupInfo()"
			:current-page.sync="params.page"
			:page-size="20"
			layout="prev, pager, next, jumper"
			:total="count">
		</el-pagination>
	</div>
</template>

<script>
    import api from '../../api'

    export default {
        name: "GroupList",
        data() {
            return {
                params: {
                    page: 1,
                    search: '',
                    type: '',
                    ordering: '',
                },
                options: [],
                tableData: [],
                count: 1,
            }
        },
        mounted() {
            api.getUserGroupType().then(data => {
                this.options = data
            });
            this.getOrUpdateGroupInfo()
        },
        methods: {
            addNewGroup() {
                console.log('addNewGroup');
                //TODO

            },
            handleEdit(index, row) {
                console.log(index, row);
                //TODO
            },
            handleCurrentChange(val) {
                console.log(`当前页: ${val}`);
                //TODO
            },
            getOrUpdateGroupInfo() {
                api.getUserGroup(this.params).then(data => {
                    this.tableData = data.results
                    this.count = data.count
                })
            },
        }
    }
</script>

<style lang="stylus">
	.group-list-wrap {
		width 100%
		height 100%

		.group-list-menu {
			width 70%
			height 40px
			margin 0 auto
			margin-top 20px

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

		.el-table {
			margin 0 auto
			margin-top 30px
			width 70%
		}

		.el-pagination {
			margin 0 auto
			width 550px
			margin-top 40px
			margin-bottom 20px
		}
	}
</style>
