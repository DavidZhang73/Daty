<template>
	<div class="home-wrap">
		<Background img-name="background.jpg"
		            :blur="false"></Background>
		<div class="home">
			<div class="button-col">
				<div class="button-row">
					<router-link :to="{name: 'fileDetail'}">
						<el-button type="primary" class="button1">
							<i class="el-icon-download"></i>
							我要收文件
						</el-button>
					</router-link>
					<router-link :to="{name: 'about'}">
						<el-button type="primary" class="button2">
							<i class="el-icon-upload2"></i>
							我要交文件
						</el-button>
					</router-link>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
    import Background from '../components/Background'

    export default {
        name: 'home',
        components: {
            Background
        }
    }
</script>

<style lang="stylus">
	.home-wrap {
		height 100%
		background-size: contain;
		background-color rgb(248,250,251)

		.home {
			height inherit

			.button-col {
				height inherit
				width 270px
				margin 0 auto
				/*border 1px solid black*/

				.button-row {
					position relative
					top 55%
					/*border 1px solid blue*/

					.button1 {
						float left
					}

					.button2 {
						float right
					}

				}
			}
		}
	}
</style>
