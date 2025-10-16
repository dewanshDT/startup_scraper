# Indian State IDs for Startup India API

This file contains state IDs that can be used in the `config.json` file to scrape startups from specific states.

## How to Use

1. Open `config.json`
2. Update the `states` array with desired state IDs
3. Or set `"scrape_all_states": true` to scrape all of India

## State IDs

| State/UT          | State ID                   |
| ----------------- | -------------------------- |
| Andhra Pradesh    | `5f48ce592a9bb065cdf9fb0d` |
| Arunachal Pradesh | `5f48ce592a9bb065cdf9fb0e` |
| Assam             | `5f48ce592a9bb065cdf9fb0f` |
| Bihar             | `5f48ce592a9bb065cdf9fb10` |
| Chhattisgarh      | `5f48ce592a9bb065cdf9fb25` |
| Goa               | `5f48ce592a9bb065cdf9fb11` |
| Gujarat           | `5f48ce592a9bb065cdf9fb12` |
| Haryana           | `5f48ce592a9bb065cdf9fb13` |
| Himachal Pradesh  | `5f48ce592a9bb065cdf9fb14` |
| Jharkhand         | `5f48ce592a9bb065cdf9fb15` |
| Karnataka         | `5f48ce592a9bb065cdf9fb16` |
| Kerala            | `5f48ce592a9bb065cdf9fb17` |
| Madhya Pradesh    | `5f48ce592a9bb065cdf9fb18` |
| Maharashtra       | `5f48ce592a9bb065cdf9fb19` |
| Manipur           | `5f48ce592a9bb065cdf9fb1a` |
| Meghalaya         | `5f48ce592a9bb065cdf9fb1b` |
| Mizoram           | `5f48ce592a9bb065cdf9fb1c` |
| Nagaland          | `5f48ce592a9bb065cdf9fb1d` |
| Odisha            | `5f48ce592a9bb065cdf9fb1e` |
| Punjab            | `5f48ce592a9bb065cdf9fb1f` |
| Rajasthan         | `5f48ce592a9bb065cdf9fb20` |
| Sikkim            | `5f48ce592a9bb065cdf9fb21` |
| Tamil Nadu        | `5f48ce592a9bb065cdf9fb22` |
| Telangana         | `5f48ce592a9bb065cdf9fb23` |
| Tripura           | `5f48ce592a9bb065cdf9fb24` |
| Uttar Pradesh     | `5f48ce592a9bb065cdf9fb26` |
| Uttarakhand       | `5f48ce592a9bb065cdf9fb27` |
| West Bengal       | `5f48ce592a9bb065cdf9fb28` |

## Union Territories

| Union Territory                          | State ID                   |
| ---------------------------------------- | -------------------------- |
| Andaman and Nicobar Islands              | `5f48ce592a9bb065cdf9fb29` |
| Chandigarh                               | `5f48ce592a9bb065cdf9fb2a` |
| Dadra and Nagar Haveli and Daman and Diu | `5f48ce592a9bb065cdf9fb2b` |
| Delhi                                    | `5f48ce592a9bb065cdf9fb2c` |
| Jammu and Kashmir                        | `5f48ce592a9bb065cdf9fb2d` |
| Ladakh                                   | `5f48ce592a9bb065cdf9fb2e` |
| Lakshadweep                              | `5f48ce592a9bb065cdf9fb2f` |
| Puducherry                               | `5f48ce592a9bb065cdf9fb30` |

## Example Configurations

### Single State (Karnataka)

```json
{
  "scrape_all_states": false,
  "states": ["5f48ce592a9bb065cdf9fb16"]
}
```

### Multiple States (Karnataka, Tamil Nadu, Maharashtra)

```json
{
  "scrape_all_states": false,
  "states": [
    "5f48ce592a9bb065cdf9fb16",
    "5f48ce592a9bb065cdf9fb22",
    "5f48ce592a9bb065cdf9fb19"
  ]
}
```

### All of India

```json
{
  "scrape_all_states": true,
  "states": []
}
```

## Notes

- The state IDs are based on the Startup India API's internal database
- Some states may have more startups than others
- When scraping all states, expect significantly longer scraping time
- The default configuration is set to Chhattisgarh

## Finding Other IDs

If you need to find IDs for other filters (industries, sectors, etc.):

1. Inspect the listing API response in `listing_api_example_response.json`
2. Look for ID fields in the nested objects
3. Add them to your payload in the scraper

## Tips

- Start with a single state to test
- For production scraping, consider rate limits
- Use `scrape_all_states: true` for comprehensive national data
