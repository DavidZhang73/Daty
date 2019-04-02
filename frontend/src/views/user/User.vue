<template>
	<div class="user-wrap">
		<Background
			img-name="background.jpg"
			:blur="true"></Background>
		<el-row style="padding-top: 120px">
			<el-col
				class="form"
				:xs="{span: 24}"
				:sm="{span: 16, offset: 4}"
				:lg="{span: 8, offset: 8}">
				<router-view></router-view>
			</el-col>
		</el-row>
	</div>
</template>

<script>
	import Background from '../../components/Background'

	export default {
		name: 'User',
		components: {
			Background
		}
	}
</script>

<style lang="stylus">
	.user-wrap {

		.form {
			padding 20px 50px 10px 50px
			border-radius 5px
			box-shadow 0 0 6px 0 rgba(0, 0, 0, 0.12)
			background-color: #ffffff
		}
	}
</style>
