<template>
      <v-flex
        xs12
        mt-5
      >
          <v-card v-if="chartData.length > 0">
            <v-toolbar
                    color="#273a56"
                    dark
            >
              <v-toolbar-title v-if="currentView">Word Cloud for Topic #{{selectedTopic}}</v-toolbar-title>
              <v-toolbar-title v-else>Topic #{{selectedTopic}} terms and weights</v-toolbar-title>
              <v-spacer></v-spacer>
              <v-select
                      style="margin-top: 25px;"
                      color="#273a56"
                      solo
                  v-if="chartData.length > 0"
                  v-model="selectedTopic"
                  :items="topicNumbers"
                  label="Topic Number Ex: 1"
                  @change="refreshChartTopic"
              />
              <v-btn
                icon
                @click="currentView = !currentView"
              >
                <v-icon>{{ currentView ? 'mdi-table' : 'mdi-chart-bubble' }}</v-icon>
              </v-btn>
            </v-toolbar>
            <highcharts v-if='currentView' :options="chartOptions"></highcharts>
              <v-data-table
                      v-else
              :headers="headers"
              :items="chartData[selectedTopic - 1]"
              hide-default-footer
              class="elevation-1"
            ></v-data-table>
          </v-card>
      </v-flex>
</template>

<script>
    export default {
        name: 'SelectCIKs',
        props: ['chartData'],
        data: () => ({
            currentView: true,
            headers: [
              { text: 'Term', value: 'term' },
              { text: 'Weight', value: 'weight' }
            ],
            selectedTopic: 1,
            topicNumbers: [],
            chartOptions: {
                accessibility: {
                    screenReaderSection: {
                        beforeChartFormat: '<h5>{chartTitle}</h5>' +
                            '<div>{chartSubtitle}</div>' +
                            '<div>{chartLongdesc}</div>' +
                            '<div>{viewTableButton}</div>'
                    }
                },
                series: [{
                    type: 'wordcloud',
                    data:  [],
                    name: 'Score'
                }],
                title: {
                    text: 'LDA generated words'
                },
                credits: {
                  enabled: false
                }
            }
        }),
        methods: {
            refreshChartTopic () {
                let seriesData = []
                this.chartData[this.selectedTopic - 1].forEach((datum) => {
                    seriesData.push({
                        name: datum.term,
                        weight: datum.weight * 100
                    })
                })
                let optionsCopy = JSON.parse(JSON.stringify(this.chartOptions))
                optionsCopy.series[0].data = seriesData
                this.chartOptions = optionsCopy
                /* eslint-disable no-console */
                console.log(this.chartOptions)
                /* eslint-enable no-console */
            }
        },
        watch: {
            chartData: function () {
                this.topicNumbers = []
                this.chartData.forEach((topic, i) => {
                    this.topicNumbers.push(i + 1)
                })
                this.refreshChartTopic()
            }
        }
    };
</script>
