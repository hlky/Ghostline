var root = Path.Combine(Path.GetTempPath(), $"ghostline-import-test-{Guid.NewGuid():N}");
Directory.CreateDirectory(root);
try
{
    var destination = Path.Combine(root, "actor.anims");
    File.WriteAllText(destination, "original");
    var rejected = await AnimationImportTransaction.RunAsync(destination, (_, staged) =>
    {
        File.WriteAllText(staged, "retargeted before failed import");
        return Task.FromResult(false);
    });
    Require(!rejected && File.ReadAllText(destination) == "original", "Rejected import replaced original");
    try
    {
        await AnimationImportTransaction.RunAsync(destination, (_, staged) =>
        {
            File.WriteAllText(staged, "partial import");
            throw new InvalidDataException("verification failed");
        });
        throw new Exception("Expected validation failure");
    }
    catch (InvalidDataException)
    {
        Require(File.ReadAllText(destination) == "original", "Validation exception replaced original");
    }
    var published = await AnimationImportTransaction.RunAsync(destination, (_, staged) =>
    {
        Require(File.ReadAllText(staged) == "original", "Import did not receive the original template");
        File.WriteAllText(staged, "verified import");
        return Task.FromResult(true);
    });
    Require(published && File.ReadAllText(destination) == "verified import", "Successful import was not published");
    Require(!Directory.EnumerateDirectories(root).Any(), "Staging directories were left behind");
    Console.WriteLine("Animation import transaction: rejection, exception, success, and cleanup passed.");
}
finally
{
    Directory.Delete(root, true);
}

static void Require(bool condition, string message)
{
    if (!condition) throw new Exception(message);
}
