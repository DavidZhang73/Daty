<template>
	<div class="user-wrap">
		<Background
			img-name="background.jpg"
			:blur="true"></Background>
		<div class="form">
			<router-view></router-view>
		</div>

	</div>
</template>

<script>
    import Background from '../../components/Background'

    export default {
        name: "User",
        components: {
            Background
        }
    }
</script>

<style lang="stylus">
	.user-wrap {

		.form {
			position absolute
			top 50%
			left 50%
			transform translate(-50%, -50%)
			min-width 400px
			padding 30px 50px 30px 50px
			border-radius 5px
			box-shadow 0 0 6px 0 rgba(0, 0, 0, 0.12)
			background-color: #ffffff
		}
	}
</style>
