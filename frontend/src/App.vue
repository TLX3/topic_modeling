<template>
  <v-app>
    <v-app-bar
      app
      color="#273a56"
      dark
    >
      <div class="d-flex align-center">
        <img

          src="topics.svg"

        />
        <div>SEC 14D9 Topic Modeling</div>
      </div>

      <v-spacer></v-spacer>
    </v-app-bar>

    <v-content>
      <Main />
    </v-content>
  </v-app>
</template>

<script>
import Main from './components/Main';
export default {
  name: 'App',
  components: {
    Main
  }
};
</script>
