param(
    [string]$OutputPath = "quests/story/ghostline/gq003/images/gq003-black-lantern-poster.png"
)

$ErrorActionPreference = "Stop"
Add-Type -AssemblyName System.Drawing

$width = 1600
$height = 2000
$bitmap = [System.Drawing.Bitmap]::new($width, $height)
$bitmap.SetResolution(144, 144)
$graphics = [System.Drawing.Graphics]::FromImage($bitmap)
$graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$graphics.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit
$graphics.CompositingQuality = [System.Drawing.Drawing2D.CompositingQuality]::HighQuality

function New-Color([int]$A, [int]$R, [int]$G, [int]$B) {
    return [System.Drawing.Color]::FromArgb($A, $R, $G, $B)
}

function New-Font([float]$Size, [System.Drawing.FontStyle]$Style = [System.Drawing.FontStyle]::Regular) {
    return [System.Drawing.Font]::new("Bahnschrift", $Size, $Style, [System.Drawing.GraphicsUnit]::Pixel)
}

function New-RoundedPath([System.Drawing.RectangleF]$Rect, [float]$Radius) {
    $path = [System.Drawing.Drawing2D.GraphicsPath]::new()
    $diameter = $Radius * 2
    $path.AddArc($Rect.X, $Rect.Y, $diameter, $diameter, 180, 90)
    $path.AddArc($Rect.Right - $diameter, $Rect.Y, $diameter, $diameter, 270, 90)
    $path.AddArc($Rect.Right - $diameter, $Rect.Bottom - $diameter, $diameter, $diameter, 0, 90)
    $path.AddArc($Rect.X, $Rect.Bottom - $diameter, $diameter, $diameter, 90, 90)
    $path.CloseFigure()
    return $path
}

function Draw-RoundedPanel(
    [System.Drawing.RectangleF]$Rect,
    [System.Drawing.Color]$Fill,
    [System.Drawing.Color]$Stroke,
    [float]$Radius = 22,
    [float]$StrokeWidth = 2
) {
    $path = New-RoundedPath $Rect $Radius
    $brush = [System.Drawing.SolidBrush]::new($Fill)
    $pen = [System.Drawing.Pen]::new($Stroke, $StrokeWidth)
    $graphics.FillPath($brush, $path)
    $graphics.DrawPath($pen, $path)
    $brush.Dispose()
    $pen.Dispose()
    $path.Dispose()
}

function Draw-Text(
    [string]$Text,
    [System.Drawing.Font]$Font,
    [System.Drawing.Color]$Color,
    [System.Drawing.RectangleF]$Rect,
    [System.Drawing.StringAlignment]$Alignment = [System.Drawing.StringAlignment]::Near,
    [System.Drawing.StringAlignment]$LineAlignment = [System.Drawing.StringAlignment]::Near
) {
    $brush = [System.Drawing.SolidBrush]::new($Color)
    $format = [System.Drawing.StringFormat]::new()
    $format.Alignment = $Alignment
    $format.LineAlignment = $LineAlignment
    $format.Trimming = [System.Drawing.StringTrimming]::EllipsisWord
    $format.FormatFlags = [System.Drawing.StringFormatFlags]::LineLimit
    $graphics.DrawString($Text, $Font, $brush, $Rect, $format)
    $format.Dispose()
    $brush.Dispose()
}

function Draw-Glow([float]$X, [float]$Y, [float]$Radius, [System.Drawing.Color]$Color) {
    for ($i = 6; $i -ge 1; $i--) {
        $r = $Radius * ($i / 6.0)
        $alpha = [int](9 + (7 - $i) * 3)
        $brush = [System.Drawing.SolidBrush]::new(
            [System.Drawing.Color]::FromArgb($alpha, $Color.R, $Color.G, $Color.B)
        )
        $graphics.FillEllipse($brush, $X - $r, $Y - $r, $r * 2, $r * 2)
        $brush.Dispose()
    }
}

function Draw-RouteNode([float]$X, [float]$Y, [System.Drawing.Color]$Color) {
    Draw-Glow $X $Y 34 $Color
    $outer = [System.Drawing.Pen]::new([System.Drawing.Color]::FromArgb(170, $Color), 3)
    $inner = [System.Drawing.SolidBrush]::new($Color)
    $graphics.DrawEllipse($outer, $X - 14, $Y - 14, 28, 28)
    $graphics.FillEllipse($inner, $X - 5, $Y - 5, 10, 10)
    $outer.Dispose()
    $inner.Dispose()
}

function Draw-ActCard(
    [int]$Number,
    [string]$Title,
    [string]$Summary,
    [System.Drawing.RectangleF]$Rect,
    [System.Drawing.Color]$Accent
) {
    Draw-RoundedPanel $Rect (New-Color 205 13 20 27) (New-Color 95 $Accent.R $Accent.G $Accent.B) 20 2

    $numberFont = New-Font 48 ([System.Drawing.FontStyle]::Bold)
    $titleFont = New-Font 23 ([System.Drawing.FontStyle]::Bold)
    $bodyFont = New-Font 19
    Draw-Text ("{0:D2}" -f $Number) $numberFont (New-Color 230 $Accent.R $Accent.G $Accent.B) `
        ([System.Drawing.RectangleF]::new($Rect.X + 26, $Rect.Y + 18, 80, 58))
    Draw-Text $Title $titleFont (New-Color 245 234 241 241) `
        ([System.Drawing.RectangleF]::new($Rect.X + 108, $Rect.Y + 24, $Rect.Width - 132, 38))
    Draw-Text $Summary $bodyFont (New-Color 205 166 180 184) `
        ([System.Drawing.RectangleF]::new($Rect.X + 108, $Rect.Y + 68, $Rect.Width - 138, 58))

    $numberFont.Dispose()
    $titleFont.Dispose()
    $bodyFont.Dispose()
}

$cyan = New-Color 255 45 219 213
$amber = New-Color 255 255 176 72
$red = New-Color 255 239 76 89
$ink = New-Color 255 6 10 15
$paper = New-Color 255 232 239 239
$muted = New-Color 255 148 165 169

try {
    # Deep atmospheric background.
    $backgroundRect = [System.Drawing.Rectangle]::new(0, 0, $width, $height)
    $background = [System.Drawing.Drawing2D.LinearGradientBrush]::new(
        $backgroundRect,
        (New-Color 255 7 12 18),
        (New-Color 255 2 5 9),
        90
    )
    $graphics.FillRectangle($background, $backgroundRect)
    $background.Dispose()

    # Subtle technical grid and rain.
    $gridPen = [System.Drawing.Pen]::new((New-Color 18 85 190 190), 1)
    for ($x = 0; $x -le $width; $x += 80) {
        $graphics.DrawLine($gridPen, $x, 0, $x, $height)
    }
    for ($y = 0; $y -le $height; $y += 80) {
        $graphics.DrawLine($gridPen, 0, $y, $width, $y)
    }
    $gridPen.Dispose()

    $rainPen = [System.Drawing.Pen]::new((New-Color 28 120 220 225), 2)
    for ($i = 0; $i -lt 95; $i++) {
        $x = (($i * 173) + 47) % $width
        $y = (($i * 281) + 71) % 760
        $len = 20 + (($i * 17) % 55)
        $graphics.DrawLine($rainPen, $x, $y, $x - 12, $y + $len)
    }
    $rainPen.Dispose()

    # Night City skyline silhouette.
    $skyline = [System.Drawing.SolidBrush]::new((New-Color 230 5 9 13))
    $buildings = @(
        @(0, 480, 170, 260), @(140, 390, 150, 350), @(270, 455, 210, 285),
        @(450, 330, 190, 410), @(620, 420, 130, 320), @(730, 300, 250, 440),
        @(950, 380, 180, 360), @(1110, 260, 210, 480), @(1300, 410, 180, 330),
        @(1460, 350, 140, 390)
    )
    foreach ($b in $buildings) {
        $graphics.FillRectangle($skyline, $b[0], $b[1], $b[2], $b[3])
    }
    $skyline.Dispose()

    # Small building lights.
    for ($i = 0; $i -lt 46; $i++) {
        $x = 35 + (($i * 137) % 1510)
        $y = 340 + (($i * 83) % 300)
        $lightColor = if (($i % 3) -eq 0) { $amber } else { $cyan }
        $light = [System.Drawing.SolidBrush]::new(
            [System.Drawing.Color]::FromArgb(80, $lightColor.R, $lightColor.G, $lightColor.B)
        )
        $graphics.FillRectangle($light, $x, $y, 9, 3)
        $light.Dispose()
    }

    # Header.
    $eyebrowFont = New-Font 32 ([System.Drawing.FontStyle]::Bold)
    $titleFont = New-Font 116 ([System.Drawing.FontStyle]::Bold)
    $subtitleFont = New-Font 31
    Draw-Text "G H O S T L I N E" $eyebrowFont $cyan `
        ([System.Drawing.RectangleF]::new(95, 62, 760, 52))
    Draw-Text "BLACK LANTERN" $titleFont $paper `
        ([System.Drawing.RectangleF]::new(86, 116, 1430, 145))
    Draw-Text "A person in pieces. A route made of people." $subtitleFont $muted `
        ([System.Drawing.RectangleF]::new(96, 264, 1070, 56))

    $badgeRect = [System.Drawing.RectangleF]::new(1115, 64, 390, 55)
    Draw-RoundedPanel $badgeRect (New-Color 210 16 29 35) (New-Color 150 45 219 213) 18 2
    $badgeFont = New-Font 18 ([System.Drawing.FontStyle]::Bold)
    Draw-Text "LONG-FORM QUEST  •  90–120 MIN" $badgeFont $paper $badgeRect `
        ([System.Drawing.StringAlignment]::Center) ([System.Drawing.StringAlignment]::Center)

    # Hero panel.
    $heroRect = [System.Drawing.RectangleF]::new(80, 335, 1440, 420)
    Draw-RoundedPanel $heroRect (New-Color 188 8 14 20) (New-Color 90 45 219 213) 30 2
    Draw-Glow 800 520 280 $cyan
    Draw-Glow 1270 545 190 $amber

    # Relay mast at left.
    $relayPen = [System.Drawing.Pen]::new((New-Color 150 45 219 213), 5)
    $graphics.DrawLine($relayPen, 245, 650, 340, 400)
    $graphics.DrawLine($relayPen, 340, 400, 435, 650)
    $graphics.DrawLine($relayPen, 278, 560, 402, 560)
    $graphics.DrawLine($relayPen, 300, 505, 380, 505)
    $graphics.DrawEllipse($relayPen, 302, 362, 76, 76)
    $graphics.DrawArc($relayPen, 270, 335, 140, 130, 205, 130)
    $relayPen.Dispose()

    # Central dignified human silhouette with fragmented memories.
    $bodyPath = [System.Drawing.Drawing2D.GraphicsPath]::new()
    $bodyPath.AddEllipse(700, 402, 200, 226)
    $bodyPath.AddBezier(720, 592, 620, 620, 590, 720, 570, 746)
    $bodyPath.AddLine(1030, 746)
    $bodyPath.AddBezier(1030, 746, 1010, 700, 970, 620, 880, 592)
    $bodyPath.CloseFigure()
    $bodyBrush = [System.Drawing.Drawing2D.LinearGradientBrush]::new(
        [System.Drawing.Rectangle]::new(570, 400, 460, 350),
        (New-Color 235 24 52 60),
        (New-Color 235 12 20 29),
        0
    )
    $bodyPen = [System.Drawing.Pen]::new((New-Color 180 45 219 213), 4)
    $graphics.FillPath($bodyBrush, $bodyPath)
    $graphics.DrawPath($bodyPen, $bodyPath)
    $bodyBrush.Dispose()
    $bodyPen.Dispose()
    $bodyPath.Dispose()

    # Memory fractures.
    $fracturePen = [System.Drawing.Pen]::new((New-Color 210 113 238 231), 3)
    $graphics.DrawLine($fracturePen, 795, 410, 770, 492)
    $graphics.DrawLine($fracturePen, 770, 492, 815, 530)
    $graphics.DrawLine($fracturePen, 815, 530, 786, 614)
    $graphics.DrawLine($fracturePen, 815, 530, 875, 486)
    $graphics.DrawLine($fracturePen, 786, 614, 748, 690)
    $fracturePen.Dispose()

    # Memory cards.
    $memoryCards = @(
        @([System.Drawing.RectangleF]::new(505, 425, 178, 88), $cyan),
        @([System.Drawing.RectangleF]::new(925, 390, 184, 92), $amber),
        @([System.Drawing.RectangleF]::new(955, 540, 205, 96), $cyan),
        @([System.Drawing.RectangleF]::new(465, 570, 190, 94), $red)
    )
    foreach ($card in $memoryCards) {
        Draw-RoundedPanel $card[0] (New-Color 190 13 23 31) `
            (New-Color 130 $card[1].R $card[1].G $card[1].B) 12 2
        $linePen = [System.Drawing.Pen]::new(
            [System.Drawing.Color]::FromArgb(100, $card[1].R, $card[1].G, $card[1].B),
            2
        )
        $graphics.DrawLine($linePen, $card[0].X + 18, $card[0].Y + 26, $card[0].Right - 18, $card[0].Y + 26)
        $graphics.DrawLine($linePen, $card[0].X + 18, $card[0].Y + 47, $card[0].Right - 48, $card[0].Y + 47)
        $graphics.DrawLine($linePen, $card[0].X + 18, $card[0].Y + 67, $card[0].Right - 76, $card[0].Y + 67)
        $linePen.Dispose()
    }

    # Stylized freight vehicle.
    $vanBrush = [System.Drawing.SolidBrush]::new((New-Color 245 17 25 32))
    $vanPen = [System.Drawing.Pen]::new((New-Color 210 255 176 72), 4)
    $graphics.FillRectangle($vanBrush, 1160, 535, 270, 120)
    $graphics.FillPolygon($vanBrush, [System.Drawing.PointF[]]@(
        [System.Drawing.PointF]::new(1100, 590),
        [System.Drawing.PointF]::new(1160, 535),
        [System.Drawing.PointF]::new(1160, 655),
        [System.Drawing.PointF]::new(1085, 655)
    ))
    $graphics.DrawRectangle($vanPen, 1160, 535, 270, 120)
    $graphics.DrawLine($vanPen, 1100, 590, 1160, 535)
    $graphics.DrawLine($vanPen, 1085, 655, 1160, 655)
    $graphics.DrawEllipse($vanPen, 1130, 630, 58, 58)
    $graphics.DrawEllipse($vanPen, 1350, 630, 58, 58)
    $vanLabelFont = New-Font 30 ([System.Drawing.FontStyle]::Bold)
    $vanLabelBrush = [System.Drawing.SolidBrush]::new($amber)
    $graphics.DrawString("07-B", $vanLabelFont, $vanLabelBrush, 1250, 570)
    $vanLabelFont.Dispose()
    $vanLabelBrush.Dispose()
    $vanBrush.Dispose()
    $vanPen.Dispose()

    # Hero route line and nodes.
    $routePen = [System.Drawing.Pen]::new((New-Color 155 45 219 213), 3)
    $routePen.DashStyle = [System.Drawing.Drawing2D.DashStyle]::Dash
    $graphics.DrawBezier($routePen, 365, 505, 520, 355, 1020, 360, 1190, 555)
    $routePen.Dispose()
    Draw-RouteNode 365 505 $cyan
    Draw-RouteNode 800 400 $cyan
    Draw-RouteNode 1190 555 $amber

    # Premise strip.
    $premiseRect = [System.Drawing.RectangleF]::new(168, 684, 1264, 88)
    Draw-RoundedPanel $premiseRect (New-Color 235 9 18 24) (New-Color 100 239 76 89) 18 2
    $premiseFont = New-Font 24 ([System.Drawing.FontStyle]::Bold)
    Draw-Text "QUIET SPINE MOVED DATA. BLACK LANTERN MOVES THE PEOPLE NEEDED TO REBUILD IT." `
        $premiseFont $paper $premiseRect ([System.Drawing.StringAlignment]::Center) `
        ([System.Drawing.StringAlignment]::Center)

    # Six-act route.
    $sectionFont = New-Font 24 ([System.Drawing.FontStyle]::Bold)
    Draw-Text "THE JOB" $sectionFont $cyan ([System.Drawing.RectangleF]::new(90, 810, 400, 42))
    $line = [System.Drawing.Pen]::new((New-Color 120 45 219 213), 2)
    $graphics.DrawLine($line, 230, 829, 1510, 829)
    $line.Dispose()

    $cardWidth = 450
    $cardHeight = 150
    $gap = 35
    $x1 = 90
    $x2 = $x1 + $cardWidth + $gap
    $x3 = $x2 + $cardWidth + $gap
    $y1 = 875
    $y2 = 1055
    Draw-ActCard 1 "THE SIGNAL" "Iris reconstructs Pair 07." `
        ([System.Drawing.RectangleF]::new($x1, $y1, $cardWidth, $cardHeight)) $cyan
    Draw-ActCard 2 "MARK THE SHIPMENT" "Trace and tag the freight transfer." `
        ([System.Drawing.RectangleF]::new($x2, $y1, $cardWidth, $cardHeight)) $amber
    Draw-ActCard 3 "RECOVER MARA" "Rescue, escort, and defend the courier." `
        ([System.Drawing.RectangleF]::new($x3, $y1, $cardWidth, $cardHeight)) $red
    Draw-ActCard 4 "STEAL PAIR 07-B" "Take the reconstruction-cipher vehicle." `
        ([System.Drawing.RectangleF]::new($x1, $y2, $cardWidth, $cardHeight)) $amber
    Draw-ActCard 5 "THE ROUTE OR THE PEOPLE" "Decide what Black Lantern becomes." `
        ([System.Drawing.RectangleF]::new($x2, $y2, $cardWidth, $cardHeight)) $cyan
    Draw-ActCard 6 "PROOF OF DESTRUCTION" "Deliver the cipher—or its ashes." `
        ([System.Drawing.RectangleF]::new($x3, $y2, $cardWidth, $cardHeight)) $red

    # Route connectors.
    $connector = [System.Drawing.Pen]::new((New-Color 95 185 214 213), 2)
    $connector.DashStyle = [System.Drawing.Drawing2D.DashStyle]::Dot
    $graphics.DrawLine($connector, 540, 950, 575, 950)
    $graphics.DrawLine($connector, 1025, 950, 1060, 950)
    $graphics.DrawLine($connector, 1285, 1025, 1285, 1055)
    $graphics.DrawLine($connector, 1060, 1130, 1025, 1130)
    $graphics.DrawLine($connector, 575, 1130, 540, 1130)
    $connector.Dispose()

    # Choice section.
    Draw-Text "THE FINAL CHOICE" $sectionFont $amber `
        ([System.Drawing.RectangleF]::new(90, 1265, 500, 42))
    $choiceRule = [System.Drawing.Pen]::new((New-Color 120 255 176 72), 2)
    $graphics.DrawLine($choiceRule, 345, 1284, 1510, 1284)
    $choiceRule.Dispose()

    $leftRect = [System.Drawing.RectangleF]::new(90, 1330, 685, 390)
    $rightRect = [System.Drawing.RectangleF]::new(825, 1330, 685, 390)
    Draw-RoundedPanel $leftRect (New-Color 215 8 25 31) (New-Color 170 45 219 213) 28 3
    Draw-RoundedPanel $rightRect (New-Color 215 30 19 13) (New-Color 180 255 176 72) 28 3

    # Choice pictograms.
    Draw-Glow 432 1436 105 $cyan
    $preservePen = [System.Drawing.Pen]::new((New-Color 220 45 219 213), 5)
    $graphics.DrawEllipse($preservePen, 382, 1386, 100, 100)
    $graphics.DrawArc($preservePen, 400, 1404, 64, 64, 35, 290)
    $graphics.DrawLine($preservePen, 432, 1410, 432, 1460)
    $preservePen.Dispose()

    Draw-Glow 1168 1436 105 $amber
    $burnPen = [System.Drawing.Pen]::new((New-Color 230 255 176 72), 5)
    $flame = [System.Drawing.Drawing2D.GraphicsPath]::new()
    $flame.AddBezier(1168, 1380, 1105, 1435, 1130, 1490, 1168, 1500)
    $flame.AddBezier(1168, 1500, 1222, 1480, 1232, 1428, 1190, 1395)
    $flame.AddBezier(1190, 1395, 1193, 1438, 1168, 1450, 1168, 1380)
    $graphics.DrawPath($burnPen, $flame)
    $burnPen.Dispose()
    $flame.Dispose()

    $choiceTitleFont = New-Font 39 ([System.Drawing.FontStyle]::Bold)
    $choiceBodyFont = New-Font 27
    Draw-Text "PRESERVE THE ROUTE" $choiceTitleFont $paper `
        ([System.Drawing.RectangleF]::new(125, 1530, 615, 58)) `
        ([System.Drawing.StringAlignment]::Center)
    Draw-Text "Find Morita. Risk the couriers." $choiceBodyFont $cyan `
        ([System.Drawing.RectangleF]::new(130, 1600, 605, 52)) `
        ([System.Drawing.StringAlignment]::Center)
    Draw-Text "BURN THE IDENTITIES" $choiceTitleFont $paper `
        ([System.Drawing.RectangleF]::new(860, 1530, 615, 58)) `
        ([System.Drawing.StringAlignment]::Center)
    Draw-Text "Protect the couriers. Lose the trail." $choiceBodyFont $amber `
        ([System.Drawing.RectangleF]::new(865, 1600, 605, 52)) `
        ([System.Drawing.StringAlignment]::Center)

    # Footer panel.
    $footerRect = [System.Drawing.RectangleF]::new(90, 1775, 1420, 140)
    Draw-RoundedPanel $footerRect (New-Color 220 10 16 22) (New-Color 70 148 165 169) 24 2
    $footerTitle = New-Font 28 ([System.Drawing.FontStyle]::Bold)
    $footerBody = New-Font 21
    Draw-Text "QUIET SPINE  →  BLACK LANTERN" $footerTitle $paper `
        ([System.Drawing.RectangleF]::new(125, 1800, 750, 48))
    Draw-Text "24 runtime-proven quest blocks • two generated scenes • five location clusters • one human cost" `
        $footerBody $muted ([System.Drawing.RectangleF]::new(125, 1852, 1180, 42))
    $tagRect = [System.Drawing.RectangleF]::new(1268, 1805, 198, 70)
    Draw-RoundedPanel $tagRect (New-Color 230 16 31 38) (New-Color 130 45 219 213) 16 2
    $tagFont = New-Font 20 ([System.Drawing.FontStyle]::Bold)
    Draw-Text "GQ003" $tagFont $cyan $tagRect `
        ([System.Drawing.StringAlignment]::Center) ([System.Drawing.StringAlignment]::Center)

    # Edge accents.
    $edgePen = [System.Drawing.Pen]::new((New-Color 180 45 219 213), 5)
    $graphics.DrawLine($edgePen, 0, 0, 0, $height)
    $edgePen.Color = New-Color 180 255 176 72
    $graphics.DrawLine($edgePen, $width - 1, 0, $width - 1, $height)
    $edgePen.Dispose()

    $outputFullPath = [System.IO.Path]::GetFullPath((Join-Path (Get-Location) $OutputPath))
    $outputDirectory = [System.IO.Path]::GetDirectoryName($outputFullPath)
    [System.IO.Directory]::CreateDirectory($outputDirectory) | Out-Null
    $bitmap.Save($outputFullPath, [System.Drawing.Imaging.ImageFormat]::Png)
    Write-Output $outputFullPath
}
finally {
    foreach ($font in @(
        $eyebrowFont, $titleFont, $subtitleFont, $badgeFont, $premiseFont,
        $sectionFont, $choiceTitleFont, $choiceBodyFont, $footerTitle,
        $footerBody, $tagFont
    )) {
        if ($null -ne $font) {
            $font.Dispose()
        }
    }
    $graphics.Dispose()
    $bitmap.Dispose()
}
