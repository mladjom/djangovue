// src/apollo.js
import { ApolloClient, InMemoryCache, HttpLink } from "@apollo/client/core";

const apolloClient = new ApolloClient({
  link: new HttpLink({
    uri: "http://127.0.0.1:8000/graphql/", // GraphQL API endpoint
  }),
  cache: new InMemoryCache(),
});

export default apolloClient;
