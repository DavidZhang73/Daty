<template>
	<div class="center-wrap">
		<Aside></Aside>
		<div class="center">
			<div class="form">
				<router-view></router-view>
			</div>
		</div>
	</div>
</template>

<script>
    import Aside from '../../components/center/Aside'

    export default {
        name: "center",
        components: {
            Aside
        }
    }
</script>

<style lang="stylus">
	.center-wrap {
		.center {
			padding 60px 0 30px 200px

			.form {
				margin 20px
				padding 20px
				background-color #fff
				border-radius 5px
				border solid 1px #e6e6e6
			}
		}
	}
</style>
