<template>
  <v-app>
    <v-app-bar
      app
      color="#273a56"
      dark
    >
      <div class="d-flex align-center">
        <v-img src="https://www.coindesk.com/wp-content/uploads/2015/11/640px-US-SecuritiesAndExchangeCommission-Seal.svg_.png" max-height="32" max-width="32" />
        <div class="ml-4">SEC 14D9 Topic Modeling</div>
      </div>
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
      },
      data: () => ({
      }),
  };
</script>
