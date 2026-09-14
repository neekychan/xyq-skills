# Campaign Occasion Routing

Identify `campaign_occasion` before writing the prompt. Default to 618 only when the user does not specify another occasion.

## Occasion Groups

- Platform campaigns: 618, 99 sale, Double 11, Double 12, Lunar New Year sale, opening sale, return sale, year-end sale, anniversary, brand day, member day, fan day, live-shopping festival, category day.
- Gift occasions: Qixi, 520, Valentine's Day, White Day, Mother's Day, Father's Day, Teachers' Day, Christmas, New Year, Spring Festival, Mid-Autumn Festival.
- Seasonal scenes: spring new arrival, summer sale, autumn/winter new arrival, seasonal change, back-to-school, graduation, travel season, camping season, commute season, renovation season, moving season.
- Category occasions: beauty day, skincare day, fragrance day, home cleaning day, appliance day, digital day, baby day, pet day, food day, apparel day, jewelry day, outdoor day, stationery day.
- Live-room specials: host special, celebrity special, factory live, warehouse live, origin live, official live room, new-customer exclusive, old-customer exclusive, 88VIP, PLUS member.

## Motive Mapping

- `618 / mid-year`: strongest price, coupon stack, gift pile, stock-up, countdown.
- `99 sale`: practical savings, daily stock-up, low-threshold coupon.
- `Double 11 / Double 12`: annual deal, cart burst, presale/deposit, full reduction, stock-up wall.
- `Qixi / 520 / Valentine's Day`: gifting, self-love, romantic limited gift, gift box.
- `Lunar New Year sale`: family stock-up, gift box, hosting, pantry restock.
- `Back-to-school`: desk/dorm/backpack setup, useful bundle, low unit price.
- `Brand day / member day`: exclusive benefit, member gift, points, official brand backing.

## Wording

Replace generic 618 wording with the current occasion:

```text
{campaign_occasion}到手¥X
{campaign_occasion}福利
{campaign_occasion}一次囤齐
```

