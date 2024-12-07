// src/graphql/queries.js
import { gql } from "graphql-tag";

export const GET_ARTICLES = gql`
  query GetArticles($first: Int, $after: String) {
    allArticles(first: $first, after: $after) {
      edges {
        node {
          id
          title
          content
          slug
        }
      }
      pageInfo {
        endCursor
        hasNextPage
      }
    }
  }
`;


export const GET_ARTICLE_BY_SLUG = gql`
query GetArticleBySlug($slug: String!) {
  articleBySlug(slug: $slug) {
    id
    title
    content
    createdAt
    slug
    category {
      id
      name
    }
    tags {
      id
      name
    }
  }
}
`;