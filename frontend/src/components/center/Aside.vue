<template>
	<div class="aside-wrap">
		<div class="aside">
			<el-menu
				router
				:default-active="$route.path"
				class="aside-menu">
				<el-submenu index="1">
					<template slot="title">
						<i class="el-icon-menu"></i>
						<span>管理</span>
					</template>
					<el-menu-item index="/center/collectionList">文件集</el-menu-item>
					<el-menu-item index="/center/groupList">用户组</el-menu-item>
				</el-submenu>
				<el-submenu index="2">
					<template slot="title">
						<i class="el-icon-setting"></i>
						<span>用户</span>
					</template>
					<el-menu-item index="/center/userInfo">修改信息</el-menu-item>
					<el-menu-item index="/center/userPassword">修改密码</el-menu-item>
				</el-submenu>
			</el-menu>
		</div>
	</div>
</template>

<script>
    export default {
        name: "Aside",
        methods: {}
    }
</script>

<style lang="stylus">
	.aside-wrap {
		position fixed
		left 0
		top 60px
		bottom 30px
		height 100%
		width 200px

		.aside {
			height 100%

			.aside-menu {
				height 100%

			}
		}


	}
</style>
